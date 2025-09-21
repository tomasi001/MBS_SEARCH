"""
Dual-panel HTML interface for MBS AI Assistant.

This module provides a comprehensive dual-panel interface with:
- Left panel: Traditional MBS code lookup
- Right panel: AI-powered natural language search
- Interactive code suggestions that populate the left panel
"""

DUAL_PANEL_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>MBS AI Assistant</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            line-height: 1.6; color: #333; background: #f5f5f5; 
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; text-align: center; 
        }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { font-size: 1.2em; opacity: 0.9; }
        
        .main-content { 
            display: grid; grid-template-columns: 1fr 1fr; gap: 30px; 
        }
        
        .panel { 
            background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); 
        }
        .panel h2 { margin-bottom: 20px; color: #333; }
        
        .input-group { margin-bottom: 20px; }
        .input-group label { display: block; margin-bottom: 8px; font-weight: 600; color: #555; }
        .input-group input, .input-group textarea { 
            width: 100%; padding: 12px; border: 2px solid #e1e5e9; border-radius: 8px; 
            font-size: 16px; transition: border-color 0.3s; 
        }
        .input-group input:focus, .input-group textarea:focus { 
            outline: none; border-color: #667eea; 
        }
        .input-group textarea { resize: vertical; min-height: 100px; }
        
        .btn { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border: none; padding: 12px 24px; border-radius: 8px; 
            cursor: pointer; font-size: 16px; font-weight: 600; transition: transform 0.2s; 
        }
        .btn:hover { transform: translateY(-2px); }
        .btn:disabled { background: #ccc; cursor: not-allowed; transform: none; }
        
        .button-group {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .btn-secondary {
            background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        }
        
        .btn-secondary:hover {
            background: linear-gradient(135deg, #545b62 0%, #343a40 100%);
        }
        
        .results { margin-top: 30px; }
        .results h3 { margin-bottom: 20px; color: #333; }
        
        .item { 
            background: white; border: 1px solid #e1e5e9; border-radius: 10px; 
            padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); 
            transition: box-shadow 0.3s; 
        }
        .item:hover { box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        
        .item-header { 
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; 
        }
        .item-title { font-size: 1.5em; font-weight: 700; color: #667eea; }
        .remove-btn { 
            background: #ff4444; color: white; border: none; border-radius: 50%; 
            width: 30px; height: 30px; cursor: pointer; font-size: 16px; font-weight: bold; 
            display: flex; align-items: center; justify-content: center; line-height: 1; 
        }
        .remove-btn:hover { background: #cc0000; }
        
        .item-details { margin-bottom: 15px; }
        .item-detail { margin-bottom: 8px; }
        .item-detail strong { color: #555; }
        
        .constraints { margin-top: 15px; }
        .constraint-group { margin-bottom: 15px; }
        .constraint-group h4 { color: #667eea; margin-bottom: 8px; font-size: 1.1em; }
        .constraint-list { list-style: none; }
        .constraint-list li { 
            background: #f8f9fa; padding: 8px 12px; margin-bottom: 5px; 
            border-radius: 5px; border-left: 4px solid #667eea; 
        }
        
        .relations { margin-top: 15px; }
        .relation { 
            background: #e3f2fd; padding: 8px 12px; margin-bottom: 5px; 
            border-radius: 5px; border-left: 4px solid #2196f3; 
        }
        .clickable-code { 
            cursor: pointer; background: #e3f2fd; border: 1px solid #2196f3; 
            padding: 2px 6px; border-radius: 3px; margin: 0 2px; 
        }
        .clickable-code:hover { background: #bbdefb; }
        
        .ai-suggestions { margin-top: 20px; }
        .suggestion { 
            background: #f0f8ff; border: 1px solid #b3d9ff; border-radius: 8px; 
            padding: 15px; margin-bottom: 15px; cursor: pointer; transition: all 0.3s; 
        }
        .suggestion:hover { 
            background: #e6f3ff; border-color: #80bfff; transform: translateY(-2px); 
        }
        .suggestion-header { 
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; 
        }
        .suggestion-code { font-size: 1.2em; font-weight: 700; color: #0066cc; }
        .suggestion-confidence { 
            background: #28a745; color: white; padding: 4px 8px; 
            border-radius: 4px; font-size: 0.9em; 
        }
        .suggestion-reasoning { color: #666; font-style: italic; margin-bottom: 10px; }
        .suggestion-requirements { margin-bottom: 10px; }
        .suggestion-requirements h5 { color: #333; margin-bottom: 5px; }
        .suggestion-requirements ul { margin-left: 20px; }
        
        .follow-up-questions { margin-top: 20px; }
        .follow-up-question { 
            background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 5px; 
            padding: 10px; margin-bottom: 10px; cursor: pointer; 
            transition: background-color 0.3s; 
        }
        .follow-up-question:hover { background: #ffeaa7; }
        
        .error { 
            background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; 
            margin: 20px 0; border: 1px solid #f5c6cb; 
        }
        .notice { 
            background: #d1ecf1; color: #0c5460; padding: 15px; border-radius: 8px; 
            margin: 20px 0; border: 1px solid #bee5eb; 
        }
        .success { 
            background: #d4edda; color: #155724; padding: 15px; border-radius: 8px; 
            margin: 20px 0; border: 1px solid #c3e6cb; 
        }
        
        .loading { text-align: center; padding: 20px; color: #666; }
        .loading::after { 
            content: ''; display: inline-block; width: 20px; height: 20px; 
            border: 2px solid #f3f3f3; border-top: 2px solid #667eea; border-radius: 50%; 
            animation: spin 1s linear infinite; margin-left: 10px; 
        }
        
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        
        .ai-status { 
            background: #e8f5e8; border: 1px solid #4caf50; border-radius: 8px; 
            padding: 15px; margin-bottom: 20px; 
        }
        .ai-status.error { background: #ffebee; border-color: #f44336; }
        .ai-status.warning { background: #fff3e0; border-color: #ff9800; }
        
        @media (max-width: 768px) {
            .main-content { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 MBS AI Assistant</h1>
            <p>Find MBS codes using natural language or traditional code lookup</p>
        </div>
        
        <div id="ai-status" class="ai-status">
            <div class="loading">Checking AI services...</div>
        </div>
        
        <div class="main-content">
            <!-- Left Panel: Traditional Code Search -->
            <div class="panel">
                <h2>🔍 Code Lookup</h2>
                <div class="input-group">
                    <label for="codes">Enter MBS item numbers (comma-separated):</label>
                    <input type="text" id="codes" placeholder="e.g., 3,23,104" />
                </div>
                <button class="btn" onclick="performCodeSearch()">🔍 Lookup Codes</button>
                
                <div id="error-left" class="error" style="display: none;"></div>
                <div id="notice-left" class="notice" style="display: none;"></div>
                
                <div id="results-left" class="results"></div>
            </div>
            
            <!-- Right Panel: Natural Language Search -->
            <div class="panel">
                <h2>🤖 AI Search</h2>
                <div class="input-group">
                    <label for="natural-query">Describe the procedure or consultation:</label>
                    <textarea id="natural-query" placeholder="e.g., 'I performed a consultation for a patient with chest pain, took history, examined them, and ordered tests'"></textarea>
                </div>
                <div class="button-group">
                    <button class="btn" onclick="performNaturalLanguageSearch()">🔍 Find Matching Codes</button>
                    <button class="btn btn-secondary" onclick="resetConversation()" style="margin-left: 10px;">🔄 Reset Chat</button>
                </div>
                
                <div id="error-right" class="error" style="display: none;"></div>
                <div id="notice-right" class="notice" style="display: none;"></div>
                
                <div id="ai-suggestions" class="ai-suggestions"></div>
                <div id="follow-up-questions" class="follow-up-questions"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Global variables
        let aiEnabled = false;
        let currentCodes = [];
        let conversationHistory = [];
        let isInChatMode = false;
        
        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            checkAIStatus();
            
            // Add enter key support for inputs
            document.getElementById('codes').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    performCodeSearch();
                }
            });
            
            document.getElementById('natural-query').addEventListener('keypress', function(e) {
                if (e.key === 'Enter' && e.ctrlKey) {
                    performNaturalLanguageSearch();
                }
            });
        });
        
        // Check AI service status
        async function checkAIStatus() {
            try {
                const response = await fetch('/api/ai/status');
                const status = await response.json();
                
                const statusDiv = document.getElementById('ai-status');
                
                if (status.ai_enabled) {
                    aiEnabled = true;
                    statusDiv.className = 'ai-status';
                    statusDiv.innerHTML = `
                        <strong>✅ AI Services Active</strong><br>
                        <small>Natural language search and vector database are available</small>
                    `;
                } else {
                    aiEnabled = false;
                    statusDiv.className = 'ai-status warning';
                    statusDiv.innerHTML = `
                        <strong>⚠️ AI Services Limited</strong><br>
                        <small>Basic code lookup available. AI features require configuration.</small>
                    `;
                }
            } catch (error) {
                aiEnabled = false;
                const statusDiv = document.getElementById('ai-status');
                statusDiv.className = 'ai-status error';
                statusDiv.innerHTML = `
                    <strong>❌ AI Services Unavailable</strong><br>
                    <small>Error: ${error.message}</small>
                `;
            }
        }
        
        // Perform natural language search
        async function performNaturalLanguageSearch() {
            const query = document.getElementById('natural-query').value.trim();
            if (!query) {
                showError('right', 'Please describe the procedure or consultation.');
                return;
            }
            
            if (!aiEnabled) {
                showError('right', 'AI services are not available. Please use code lookup instead.');
                return;
            }
            
            showLoading('right', 'Searching for matching MBS codes...');
            
            try {
                let response;
                
                if (isInChatMode && conversationHistory.length > 0) {
                    // Use conversational endpoint
                    response = await fetch('/api/ai/conversation', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ 
                            query: query,
                            conversation_history: conversationHistory
                        })
                    });
                } else {
                    // Use regular endpoint
                    response = await fetch('/api/ai/natural-language', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ query })
                    });
                }
                
                const data = await response.json();
                
                // Add to conversation history
                conversationHistory.push({
                    type: 'user',
                    content: query,
                    timestamp: new Date().toISOString()
                });
                
                if (data.suggested_codes && data.suggested_codes.length > 0) {
                    displayAISuggestions(data.detailed_suggestions);
                    displayFollowUpQuestions(data.follow_up_questions);
                    
                    // Add assistant response to conversation history
                    conversationHistory.push({
                        type: 'assistant',
                        content: `Found ${data.suggested_codes.length} matching codes`,
                        suggested_codes: data.suggested_codes,
                        timestamp: new Date().toISOString()
                    });
                    
                    showSuccess('right', `Found ${data.suggested_codes.length} matching MBS codes`);
                    isInChatMode = true; // Enable chat mode after first search
                } else {
                    showNotice('right', 'No matching codes found. Try providing more specific details about the procedure.');
                }
                
            } catch (error) {
                showError('right', 'Search failed: ' + error.message);
            }
        }
        
        // Perform code number search
        async function performCodeSearch() {
            const codesInput = document.getElementById('codes').value.trim();
            if (!codesInput) {
                showError('left', 'Please enter one or more MBS item numbers.');
                return;
            }
            
            const codes = codesInput.split(',').map(c => c.trim()).filter(c => c);
            if (codes.length === 0) {
                showError('left', 'Please enter valid MBS item numbers.');
                return;
            }
            
            showLoading('left', 'Looking up MBS codes...');
            
            try {
                const response = await fetch('/api/items?codes=' + encodeURIComponent(codes.join(',')));
                const data = await response.json();
                
                if (data.items && data.items.length > 0) {
                    displayResults(data.items);
                    currentCodes = codes;
                    showSuccess('left', `Found ${data.items.length} MBS codes`);
                } else {
                    showNotice('left', 'No codes found. Please check the item numbers.');
                }
                
            } catch (error) {
                showError('left', 'Lookup failed: ' + error.message);
            }
        }
        
        // Display AI suggestions
        function displayAISuggestions(suggestions) {
            const container = document.getElementById('ai-suggestions');
            
            if (!suggestions || suggestions.length === 0) {
                container.innerHTML = '';
                return;
            }
            
            let html = '<h3>🤖 AI Suggestions</h3>';
            
            suggestions.forEach(suggestion => {
                html += `
                    <div class="suggestion" onclick="addCodeToLeftPanel('${suggestion.code}')">
                        <div class="suggestion-header">
                            <span class="suggestion-code">Code ${suggestion.code}</span>
                            <span class="suggestion-confidence">${Math.round(suggestion.confidence * 100)}% match</span>
                        </div>
                        <div class="suggestion-reasoning">${suggestion.reasoning}</div>
                        ${suggestion.requirements.length > 0 ? `
                            <div class="suggestion-requirements">
                                <h5>Requirements:</h5>
                                <ul>
                                    ${suggestion.requirements.map(req => `<li>${req}</li>`).join('')}
                                </ul>
                            </div>
                        ` : ''}
                        ${suggestion.exclusions.length > 0 ? `
                            <div class="suggestion-requirements">
                                <h5>Exclusions:</h5>
                                <ul>
                                    ${suggestion.exclusions.map(exc => `<li>${exc}</li>`).join('')}
                                </ul>
                            </div>
                        ` : ''}
                    </div>
                `;
            });
            
            container.innerHTML = html;
        }
        
        // Display follow-up questions
        function displayFollowUpQuestions(questions) {
            const container = document.getElementById('follow-up-questions');
            
            if (!questions || questions.length === 0) {
                container.innerHTML = '';
                return;
            }
            
            let html = '<h3>❓ Follow-up Questions</h3>';
            
            questions.forEach(question => {
                html += `
                    <div class="follow-up-question" onclick="askFollowUpQuestion('${question}')">
                        ${question}
                    </div>
                `;
            });
            
            container.innerHTML = html;
        }
        
        // Ask follow-up question
        function askFollowUpQuestion(question) {
            document.getElementById('natural-query').value = question;
            performNaturalLanguageSearch();
        }
        
        // Reset conversation
        function resetConversation() {
            conversationHistory = [];
            isInChatMode = false;
            document.getElementById('natural-query').value = '';
            document.getElementById('ai-suggestions').innerHTML = '';
            document.getElementById('follow-up-questions').innerHTML = '';
            showNotice('right', 'Conversation reset. Start a new search.');
        }
        
        // Add code to left panel
        function addCodeToLeftPanel(code) {
            const inputField = document.getElementById('codes');
            const currentCodes = inputField.value ? inputField.value.split(',').map(c => c.trim()) : [];
            
            if (!currentCodes.includes(code)) {
                currentCodes.push(code);
                inputField.value = currentCodes.join(', ');
                performCodeSearch();
            }
        }
        
        // Display search results
        function displayResults(items) {
            const container = document.getElementById('results-left');
            
            if (!items || items.length === 0) {
                container.innerHTML = '';
                return;
            }
            
            let html = '<h3>📋 MBS Code Results</h3>';
            
            items.forEach(item => {
                html += `
                    <div class="item" data-item-code="${item.item.item_num}">
                        <div class="item-header">
                            <span class="item-title">MBS Code ${item.item.item_num}</span>
                            <button class="remove-btn" data-item-code="${item.item.item_num}">✕</button>
                        </div>
                        
                        <div class="item-details">
                            <div class="item-detail"><strong>Category:</strong> ${item.item.category}</div>
                            <div class="item-detail"><strong>Fee:</strong> $${item.item.schedule_fee}</div>
                            <div class="item-detail"><strong>Description:</strong> ${item.item.description}</div>
                        </div>
                        
                        ${item.constraints && item.constraints.length > 0 ? `
                            <div class="constraints">
                                <h4>📋 Requirements & Constraints</h4>
                                ${groupConstraints(item.constraints)}
                            </div>
                        ` : ''}
                        
                        ${item.relations && item.relations.length > 0 ? `
                            <div class="relations">
                                <h4>🔗 Related Codes</h4>
                                ${item.relations.map(rel => `
                                    <div class="relation">
                                        <strong>${rel.relation_type}:</strong> 
                                        ${rel.target_item_num ? `<span class="clickable-code" data-target-code="${rel.target_item_num}">${rel.target_item_num}</span>` : ''}
                                        ${rel.detail ? ` - ${rel.detail}` : ''}
                                    </div>
                                `).join('')}
                            </div>
                        ` : ''}
                    </div>
                `;
            });
            
            container.innerHTML = html;
            
            // Add event listeners for interactive elements
            addInteractiveListeners();
        }
        
        // Group constraints by type
        function groupConstraints(constraints) {
            const groups = {};
            
            constraints.forEach(constraint => {
                const type = constraint.constraint_type;
                if (!groups[type]) {
                    groups[type] = [];
                }
                groups[type].push(constraint.value);
            });
            
            let html = '';
            Object.keys(groups).forEach(type => {
                html += `
                    <div class="constraint-group">
                        <h4>${type.replace(/_/g, ' ').toUpperCase()}</h4>
                        <ul class="constraint-list">
                            ${groups[type].map(value => `<li>${value}</li>`).join('')}
                        </ul>
                    </div>
                `;
            });
            
            return html;
        }
        
        // Add interactive listeners
        function addInteractiveListeners() {
            // Remove button listeners
            document.querySelectorAll('.remove-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const itemCode = this.getAttribute('data-item-code');
                    removeItem(itemCode);
                });
            });
            
            // Clickable code listeners
            document.querySelectorAll('.clickable-code').forEach(code => {
                code.addEventListener('click', function() {
                    const targetCode = this.getAttribute('data-target-code');
                    addCodeToLeftPanel(targetCode);
                });
            });
        }
        
        // Remove item
        function removeItem(itemCode) {
                const itemElement = document.querySelector(`[data-item-code="${itemCode}"]`);
                if (itemElement && itemElement.parentNode) {
                    itemElement.parentNode.removeChild(itemElement);
                    updateInputField();
                }
        }
        
        // Update input field
        function updateInputField() {
            const displayedItems = document.querySelectorAll('.item');
            const codes = [];
            displayedItems.forEach(item => {
                const code = item.getAttribute('data-item-code');
                if (code) {
                    codes.push(code);
                }
            });
            
            const inputField = document.getElementById('codes');
            if (inputField) {
                inputField.value = codes.join(', ');
            }
        }
        
        // Utility functions
        function showError(side, message) {
            const errorDiv = document.getElementById(`error-${side}`);
            errorDiv.textContent = message;
            errorDiv.style.display = 'block';
            document.getElementById(`notice-${side}`).style.display = 'none';
        }
        
        function showNotice(side, message) {
            const noticeDiv = document.getElementById(`notice-${side}`);
            noticeDiv.textContent = message;
            noticeDiv.style.display = 'block';
            document.getElementById(`error-${side}`).style.display = 'none';
        }
        
        function showSuccess(side, message) {
            const noticeDiv = document.getElementById(`notice-${side}`);
            noticeDiv.textContent = message;
            noticeDiv.className = 'success';
            noticeDiv.style.display = 'block';
            document.getElementById(`error-${side}`).style.display = 'none';
        }
        
        function showLoading(side, message) {
            const noticeDiv = document.getElementById(`notice-${side}`);
            noticeDiv.innerHTML = `<div class="loading">${message}</div>`;
            noticeDiv.style.display = 'block';
            document.getElementById(`error-${side}`).style.display = 'none';
        }
    </script>
</body>
</html>
"""
