from mbs_clarity.mbs_parser import parse_csv


def test_parse_csv_maps_fields(tmp_path):
    p = tmp_path / "mini.csv"
    p.write_text(
        'ItemNum,Category,Group,ScheduleFee,Description\n"3","1","A1","20.05","Desc"\n'
    )
    items = parse_csv(str(p))
    assert items[0]["item_num"] == "3"
    assert items[0]["schedule_fee"] == 20.05
