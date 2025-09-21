"""
Enhanced ChatGPT-style UI for MBS AI Assistant with conversational interface.
"""

ENHANCED_CHAT_UI = """
<!DOCTYPE html>
<html>
<head>
    <title>MBS AI Assistant - Enhanced Chat</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            line-height: 1.6; color: #333; background: #f7f7f8; height: 100vh;
            display: flex; flex-direction: column;
        }
        
        .header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; padding: 20px; text-align: center; flex-shrink: 0;
        }
        .header h1 { font-size: 1.8em; margin-bottom: 5px; }
        .header p { font-size: 1em; opacity: 0.9; }
        
        .main-container {
            display: flex; flex: 1; overflow: hidden;
        }
        
        .left-panel {
            width: 40%; background: white; border-right: 1px solid #e1e5e9;
            display: flex; flex-direction: column;
        }
        
        .right-panel {
            width: 60%; background: #f7f7f8; display: flex; flex-direction: column;
        }
        
        .panel-header {
            padding: 20px; border-bottom: 1px solid #e1e5e9; background: white;
            font-weight: 600; font-size: 1.1em;
        }
        
        .chat-container {
            flex: 1; display: flex; flex-direction: column; overflow: hidden;
        }
        
        .chat-messages {
            flex: 1; overflow-y: auto; padding: 20px; background: #f7f7f8;
        }
        
        .message {
            margin-bottom: 20px; display: flex; align-items: flex-start;
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message.assistant {
            justify-content: flex-start;
        }
        
        .message-content {
            max-width: 70%; padding: 12px 16px; border-radius: 18px;
            word-wrap: break-word;
        }
        
        .message.user .message-content {
            background: #007bff; color: white; border-bottom-right-radius: 4px;
        }
        
        .message.assistant .message-content {
            background: white; color: #333; border: 1px solid #e1e5e9;
            border-bottom-left-radius: 4px;
        }
        
        .message-time {
            font-size: 0.8em; color: #666; margin-top: 4px;
        }
        
        .chat-input-container {
            padding: 20px; background: white; border-top: 1px solid #e1e5e9;
            flex-shrink: 0;
        }
        
        .chat-input-wrapper {
            display: flex; align-items: flex-end; gap: 10px;
            background: #f7f7f8; border-radius: 24px; padding: 8px;
            border: 1px solid #e1e5e9;
        }
        
        .chat-input {
            flex: 1; border: none; background: transparent; padding: 12px 16px;
            font-size: 16px; resize: none; outline: none; min-height: 24px;
            max-height: 120px; font-family: inherit;
        }
        
        .chat-send-btn {
            background: #007bff; color: white; border: none; border-radius: 50%;
            width: 40px; height: 40px; cursor: pointer; display: flex;
            align-items: center; justify-content: center; font-size: 18px;
            transition: background 0.2s;
        }
        
        .chat-send-btn:hover {
            background: #0056b3;
        }
        
        .chat-send-btn:disabled {
            background: #ccc; cursor: not-allowed;
        }
        
        .code-search-section {
            padding: 20px; flex: 1; overflow-y: auto;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        .input-group label {
            display: block; margin-bottom: 8px; font-weight: 500; color: #333;
        }
        
        .input-group input {
            width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 8px;
            font-size: 16px; font-family: inherit;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border: none; padding: 12px 24px; border-radius: 8px; 
            cursor: pointer; font-size: 16px; font-weight: 600; transition: transform 0.2s;
            margin-right: 10px;
        }
        .btn:hover { transform: translateY(-2px); }
        .btn:disabled { background: #ccc; cursor: not-allowed; transform: none; }
        
        .btn-secondary {
            background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        }
        .btn-secondary:hover {
            background: linear-gradient(135deg, #545b62 0%, #343a40 100%);
        }
        
        .results {
            margin-top: 20px;
        }
        
        .item {
            background: white; border: 1px solid #e1e5e9; border-radius: 10px; 
            padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .item-header {
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 15px;
        }
        
        .item-title {
            font-weight: 600; font-size: 1.1em; color: #333;
        }
        
        .remove-btn {
            background: #dc3545; color: white; border: none; border-radius: 50%;
            width: 30px; height: 30px; cursor: pointer; font-size: 14px;
        }
        
        .item-details {
            margin-bottom: 15px;
        }
        
        .item-detail {
            margin-bottom: 8px; color: #666;
        }
        
        .clickable-code {
            color: #007bff; cursor: pointer; text-decoration: underline;
        }
        
        .clickable-code:hover {
            color: #0056b3;
        }
        
        .ai-suggestions {
            margin-top: 20px;
        }
        
        .suggestion {
            background: white; border: 1px solid #e1e5e9; border-radius: 10px;
            padding: 15px; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .suggestion-header {
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 10px;
        }
        
        .suggestion-code {
            font-weight: 600; color: #007bff; cursor: pointer;
        }
        
        .suggestion-confidence {
            background: #28a745; color: white; padding: 4px 8px; border-radius: 12px;
            font-size: 0.8em;
        }
        
        .suggestion-reasoning {
            color: #666; font-size: 0.9em; margin-bottom: 10px;
        }
        
        .follow-up-prompt {
            background: #e3f2fd; border: 1px solid #2196f3; border-radius: 10px;
            padding: 15px; margin-top: 20px;
        }
        
        .follow-up-prompt h4 {
            color: #1976d2; margin-bottom: 10px;
        }
        
        .follow-up-suggestion {
            background: white; border: 1px solid #2196f3; border-radius: 8px;
            padding: 10px; margin-bottom: 8px; cursor: pointer;
            transition: background 0.2s;
        }
        
        .follow-up-suggestion:hover {
            background: #f3f9ff;
        }
        
        .error {
            background: #f8d7da; color: #721c24; padding: 12px; border-radius: 8px;
            margin-bottom: 15px; border: 1px solid #f5c6cb;
        }
        
        .notice {
            background: #d1ecf1; color: #0c5460; padding: 12px; border-radius: 8px;
            margin-bottom: 15px; border: 1px solid #bee5eb;
        }
        
        .success {
            background: #d4edda; color: #155724; padding: 12px; border-radius: 8px;
            margin-bottom: 15px; border: 1px solid #c3e6cb;
        }
        
        .loading {
            display: flex; align-items: center; gap: 10px;
            color: #666; font-style: italic;
        }
        
        .loading::after {
            content: ''; width: 20px; height: 20px; border: 2px solid #f3f3f3;
            border-top: 2px solid #007bff; border-radius: 50%; animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .ai-status {
            padding: 15px; margin-bottom: 20px; border-radius: 8px;
            text-align: center; font-weight: 500;
        }
        
        .ai-status.enabled {
            background: #d4edda; color: #155724; border: 1px solid #c3e6cb;
        }
        
        .ai-status.disabled {
            background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb;
        }
        
        .constraints, .relations {
            margin-top: 15px;
        }
        
        .constraints h4, .relations h4 {
            color: #333; margin-bottom: 10px; font-size: 1em;
        }
        
        .constraint-group {
            background: #f8f9fa; padding: 10px; border-radius: 6px; margin-bottom: 8px;
        }
        
        .constraint-type {
            font-weight: 600; color: #495057;
        }
        
        .relation {
            margin-bottom: 8px; color: #666;
        }
        
        .relation-type {
            font-weight: 600; color: #495057;
        }
        
        .empty-state {
            text-align: center; color: #666; padding: 40px 20px;
        }
        
        .empty-state h3 {
            margin-bottom: 10px; color: #333;
        }
        
        .empty-state p {
            font-size: 0.9em; line-height: 1.5;
        }
        
        @media (max-width: 768px) {
            .main-container {
                flex-direction: column;
            }
            
            .left-panel, .right-panel {
                width: 100%;
            }
            
            .left-panel {
                height: 40vh;
            }
            
            .right-panel {
                height: 60vh;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 MBS AI Assistant</h1>
        <p>Find the right MBS codes using natural language or lookup specific items</p>
    </div>
    
    <div class="main-container">
        <!-- Left Panel: Code Number Search -->
        <div class="left-panel">
            <div class="panel-header">
                📋 MBS Code Lookup
            </div>
            <div class="code-search-section">
                <div id="ai-status" class="ai-status">
                    <div class="loading">Checking AI services...</div>
                </div>
                
                <div class="input-group">
                    <label for="codes">Enter MBS item numbers (comma-separated):</label>
                    <input type="text" id="codes" placeholder="e.g., 3,23,104" />
                </div>
                
                <div class="button-group">
                    <button class="btn" onclick="performCodeSearch()">🔍 Lookup Codes</button>
                    <button class="btn btn-secondary" onclick="clearCodeSearch()">🗑️ Clear</button>
                </div>
                
                <div id="code-search-error" class="error" style="display: none;"></div>
                <div id="code-search-notice" class="notice" style="display: none;"></div>
                
                <div id="code-search-results" class="results"></div>
            </div>
        </div>
        
        <!-- Right Panel: AI Chat -->
        <div class="right-panel">
            <div class="panel-header">
                💬 AI Assistant Chat
            </div>
            <div class="chat-container">
                <div class="chat-messages" id="chat-messages">
                    <div class="empty-state">
                        <h3>👋 Welcome to MBS AI Assistant!</h3>
                        <p>I can help you find the right MBS codes for medical procedures, consultations, and treatments. Just describe what you did in natural language, and I'll suggest the most appropriate codes.</p>
                        <br>
                        <p><strong>Try asking:</strong></p>
                        <p>"I performed a consultation for a patient with chest pain"</p>
                        <p>"I did a comprehensive examination of a patient"</p>
                        <p>"I performed surgery on a patient's knee"</p>
                    </div>
                </div>
                
                <div class="chat-input-container">
                    <div class="chat-input-wrapper">
                        <textarea 
                            id="chat-input" 
                            class="chat-input" 
                            placeholder="Describe the medical procedure or consultation..."
                            rows="1"
                        ></textarea>
                        <button id="chat-send-btn" class="chat-send-btn" onclick="sendMessage()">
                            ➤
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Global variables
        let aiEnabled = false;
        let conversationHistory = [];
        let isProcessing = false;
        
        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            checkAIStatus();
            setupEventListeners();
        });
        
        function setupEventListeners() {
            const chatInput = document.getElementById('chat-input');
            const chatSendBtn = document.getElementById('chat-send-btn');
            
            // Auto-resize textarea
            chatInput.addEventListener('input', function() {
                this.style.height = 'auto';
                this.style.height = Math.min(this.scrollHeight, 120) + 'px';
            });
            
            // Send message on Enter (but not Shift+Enter)
            chatInput.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    sendMessage();
                }
            });
            
            // Send button click
            chatSendBtn.addEventListener('click', sendMessage);
            
            // Code input Enter key
            document.getElementById('codes').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    performCodeSearch();
                }
            });
        }
        
        async function checkAIStatus() {
            try {
                const response = await fetch('/api/ai/status');
                const data = await response.json();
                
                aiEnabled = data.ai_enabled;
                
                const statusElement = document.getElementById('ai-status');
                if (aiEnabled) {
                    statusElement.className = 'ai-status enabled';
                    statusElement.innerHTML = '✅ AI services are ready';
                } else {
                    statusElement.className = 'ai-status disabled';
                    statusElement.innerHTML = '❌ AI services unavailable';
                }
            } catch (error) {
                const statusElement = document.getElementById('ai-status');
                statusElement.className = 'ai-status disabled';
                statusElement.innerHTML = '❌ Error checking AI status';
            }
        }
        
        async function sendMessage() {
            const chatInput = document.getElementById('chat-input');
            const message = chatInput.value.trim();
            
            if (!message || isProcessing) return;
            
            // Clear input
            chatInput.value = '';
            chatInput.style.height = 'auto';
            
            // Add user message to chat
            addMessageToChat('user', message);
            
            // Show processing state
            setProcessingState(true);
            
            try {
                let response;
                
                if (conversationHistory.length > 0) {
                    // Use conversational endpoint
                    response = await fetch('/api/ai/conversation', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ 
                            query: message,
                            conversation_history: conversationHistory
                        })
                    });
                } else {
                    // Use regular endpoint
                    response = await fetch('/api/ai/natural-language', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ query: message })
                    });
                }
                
                const data = await response.json();
                
                // Add to conversation history
                conversationHistory.push({
                    type: 'user',
                    content: message,
                    timestamp: new Date().toISOString()
                });
                
                if (data.error) {
                    // Handle error response
                    addMessageToChat('assistant', `❌ ${data.error}`);
                } else if (data.suggested_codes && data.suggested_codes.length > 0) {
                    // Handle successful response with suggestions
                    const responseText = `I found ${data.suggested_codes.length} MBS codes that match your description:`;
                    addMessageToChat('assistant', responseText);
                    
                    // Add suggestions
                    addSuggestionsToChat(data.detailed_suggestions);
                    
                    // Add follow-up prompts
                    if (data.follow_up_questions && data.follow_up_questions.length > 0) {
                        addFollowUpPromptsToChat(data.follow_up_questions);
                    }
                    
                    // Add assistant response to conversation history
                    conversationHistory.push({
                        type: 'assistant',
                        content: responseText,
                        suggested_codes: data.suggested_codes,
                        timestamp: new Date().toISOString()
                    });
                } else {
                    // No suggestions found
                    addMessageToChat('assistant', "I couldn't find any matching MBS codes for that description. Could you provide more details about the procedure or consultation?");
                }
                
            } catch (error) {
                addMessageToChat('assistant', `❌ Sorry, there was an error processing your request: ${error.message}`);
            } finally {
                setProcessingState(false);
            }
        }
        
        function addMessageToChat(type, content) {
            const chatMessages = document.getElementById('chat-messages');
            
            // Remove empty state if it exists
            const emptyState = chatMessages.querySelector('.empty-state');
            if (emptyState) {
                emptyState.remove();
            }
            
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${type}`;
            
            const time = new Date().toLocaleTimeString();
            
            messageDiv.innerHTML = `
                <div class="message-content">
                    ${content}
                    <div class="message-time">${time}</div>
                </div>
            `;
            
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function addSuggestionsToChat(suggestions) {
            const chatMessages = document.getElementById('chat-messages');
            
            const suggestionsDiv = document.createElement('div');
            suggestionsDiv.className = 'message assistant';
            
            let html = '<div class="message-content"><div class="ai-suggestions">';
            
            suggestions.forEach(suggestion => {
                html += `
                    <div class="suggestion">
                        <div class="suggestion-header">
                            <span class="suggestion-code clickable-code" onclick="addCodeToLeftPanel('${suggestion.code}')">
                                ${suggestion.code}
                            </span>
                            <span class="suggestion-confidence">${suggestion.confidence}% match</span>
                        </div>
                        <div class="suggestion-reasoning">${suggestion.reasoning}</div>
                        <div style="font-size: 0.9em; color: #666; margin-top: 8px;">
                            ${suggestion.description}
                        </div>
                    </div>
                `;
            });
            
            html += '</div></div>';
            suggestionsDiv.innerHTML = html;
            
            chatMessages.appendChild(suggestionsDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function addFollowUpPromptsToChat(questions) {
            const chatMessages = document.getElementById('chat-messages');
            
            const promptsDiv = document.createElement('div');
            promptsDiv.className = 'message assistant';
            
            let html = `
                <div class="message-content">
                    <div class="follow-up-prompt">
                        <h4>💡 To help me find more specific codes, please provide:</h4>
            `;
            
            questions.forEach(question => {
                html += `
                    <div class="follow-up-suggestion" onclick="useFollowUpPrompt('${question.replace(/'/g, "\\'")}')">
                        ${question}
                    </div>
                `;
            });
            
            html += '</div></div>';
            promptsDiv.innerHTML = html;
            
            chatMessages.appendChild(promptsDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function useFollowUpPrompt(question) {
            const chatInput = document.getElementById('chat-input');
            chatInput.value = question;
            chatInput.focus();
            chatInput.style.height = 'auto';
            chatInput.style.height = Math.min(chatInput.scrollHeight, 120) + 'px';
        }
        
        function setProcessingState(processing) {
            isProcessing = processing;
            const sendBtn = document.getElementById('chat-send-btn');
            const chatInput = document.getElementById('chat-input');
            
            if (processing) {
                sendBtn.disabled = true;
                chatInput.disabled = true;
                sendBtn.innerHTML = '⏳';
            } else {
                sendBtn.disabled = false;
                chatInput.disabled = false;
                sendBtn.innerHTML = '➤';
            }
        }
        
        // Code search functionality (unchanged)
        async function performCodeSearch() {
            const codesInput = document.getElementById('codes').value.trim();
            if (!codesInput) {
                showError('code-search-error', 'Please enter one or more MBS item numbers.');
                return;
            }
            
            const codes = codesInput.split(',').map(c => c.trim()).filter(c => c);
            if (codes.length === 0) {
                showError('code-search-error', 'Please enter valid MBS item numbers.');
                return;
            }
            
            showLoading('code-search-notice', 'Looking up MBS codes...');
            
            try {
                const response = await fetch('/api/items?codes=' + encodeURIComponent(codes.join(',')));
                const data = await response.json();
                
                if (data.items && data.items.length > 0) {
                    displayResults(data.items);
                    showSuccess('code-search-notice', `Found ${data.items.length} MBS codes`);
                } else {
                    showNotice('code-search-notice', 'No codes found. Please check the item numbers.');
                }
                
            } catch (error) {
                showError('code-search-error', 'Lookup failed: ' + error.message);
            } finally {
                hideLoading('code-search-notice');
            }
        }
        
        function clearCodeSearch() {
            document.getElementById('codes').value = '';
            document.getElementById('code-search-results').innerHTML = '';
            hideMessages(['code-search-error', 'code-search-notice']);
        }
        
        function addCodeToLeftPanel(code) {
            const inputField = document.getElementById('codes');
            const currentCodes = inputField.value ? inputField.value.split(',').map(c => c.trim()) : [];
            
            if (!currentCodes.includes(code)) {
                currentCodes.push(code);
                inputField.value = currentCodes.join(', ');
                performCodeSearch();
            }
        }
        
        function displayResults(items) {
            const container = document.getElementById('code-search-results');
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
                            <button class="remove-btn" onclick="removeItem('${item.item.item_num}')">✕</button>
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
                                        ${rel.target_item_num ? `<span class="clickable-code" onclick="addCodeToLeftPanel('${rel.target_item_num}')">${rel.target_item_num}</span>` : ''}
                                        ${rel.detail ? ` - ${rel.detail}` : ''}
                                    </div>
                                `).join('')}
                            </div>
                        ` : ''}
                    </div>
                `;
            });
            
            container.innerHTML = html;
        }
        
        function removeItem(itemCode) {
                const itemElement = document.querySelector(`[data-item-code="${itemCode}"]`);
                if (itemElement) {
                    itemElement.remove();
                    updateLeftPanelInputField();
                }
        }
        
        function updateLeftPanelInputField() {
            const displayedItems = document.querySelectorAll('#code-search-results .item');
            const codes = [];
            displayedItems.forEach(item => {
                const code = item.getAttribute('data-item-code');
                if (code) {
                    codes.push(code);
                }
            });
            
            const inputField = document.getElementById('codes');
            inputField.value = codes.join(', ');
        }
        
        function groupConstraints(constraints) {
            const grouped = {};
            constraints.forEach(constraint => {
                const type = constraint.constraint_type;
                if (!grouped[type]) {
                    grouped[type] = [];
                }
                grouped[type].push(constraint.value);
            });
            
            let html = '';
            Object.keys(grouped).forEach(type => {
                html += `
                    <div class="constraint-group">
                        <div class="constraint-type">${type}:</div>
                        <div>${grouped[type].join(', ')}</div>
                    </div>
                `;
            });
            
            return html;
        }
        
        // Utility functions
        function showError(targetId, message) {
            const element = document.getElementById(targetId);
            element.innerHTML = message;
            element.style.display = 'block';
        }
        
        function showNotice(targetId, message) {
            const element = document.getElementById(targetId);
            element.innerHTML = message;
            element.style.display = 'block';
        }
        
        function showSuccess(targetId, message) {
            const element = document.getElementById(targetId);
            element.innerHTML = message;
            element.style.display = 'block';
        }
        
        function showLoading(targetId, message) {
            const element = document.getElementById(targetId);
            element.innerHTML = `<div class="loading">${message}</div>`;
            element.style.display = 'block';
        }
        
        function hideLoading(targetId) {
            const element = document.getElementById(targetId);
            element.style.display = 'none';
        }
        
        function hideMessages(targetIds) {
            targetIds.forEach(id => {
                const element = document.getElementById(id);
                if (element) {
                    element.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
"""
