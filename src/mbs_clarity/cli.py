import argparse
from collections import Counter, defaultdict

from lxml import etree


def _profile_xml(xml_path: str):
    with open(xml_path, "rb") as f:
        tree = etree.parse(f)
    root = tree.getroot()
    # Count local-names under item nodes
    items = root.xpath(
        "//*[ *[local-name()='ItemNum' or local-name()='ItemNumber' or local-name()='Item' or local-name()='Number'] ]"
    )
    tag_counts = Counter()
    sample_values = defaultdict(list)
    for node in items[:200]:  # limit to 200 for speed
        for child in node.iterchildren():
            ln = etree.QName(child).localname
            tag_counts[ln] += 1
            if len(sample_values[ln]) < 3:
                txt = (child.text or "").strip()
                if txt:
                    sample_values[ln].append(txt)
    print(f"Items detected: {len(items)}")
    print("Top tags under items:")
    for tag, cnt in tag_counts.most_common(20):
        smp = "; ".join(sample_values[tag])
        print(f"  {tag}: {cnt}  e.g., {smp}")


def main():
    parser = argparse.ArgumentParser(description="MBS Clarity CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    load = sub.add_parser("load", help="Load MBS data into SQLite")
    load.add_argument("--xml", type=str, default=None)
    load.add_argument("--csv", type=str, default=None)

    analyze = sub.add_parser("analyze-xml", help="Profile XML structure and content")
    analyze.add_argument("path", type=str)

    args = parser.parse_args()

    if args.cmd == "load":
        from mbs_clarity._loader import main as load_main

        return load_main()
    if args.cmd == "analyze-xml":
        return _profile_xml(args.path)


if __name__ == "__main__":
    main()
