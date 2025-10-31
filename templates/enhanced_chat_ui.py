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
            display: flex; flex-direction: column; margin: 0; padding: 0; overflow: hidden;
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
            font-weight: 600; font-size: 1.1em; display: flex; justify-content: space-between; align-items: center;
        }
        
        .ai-status-header {
            font-size: 0.9em; font-weight: 500;
        }
        
        .ai-status-header .loading {
            color: #666; font-style: italic;
        }
        
        .ai-status-header .loading::after {
            content: ''; width: 16px; height: 16px; border: 2px solid #f3f3f3;
            border-top: 2px solid #007bff; border-radius: 50%; animation: spin 1s linear infinite;
            display: inline-block; margin-left: 8px; vertical-align: middle;
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
            flex: 1; border: none; background: transparent; padding: 2px 6px;
            font-size: 16px; resize: none; outline: none; min-height: 48px;
            max-height: 25vh; font-family: inherit; overflow-y: auto;
            line-height: 1.4;
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
        
        .search-container {
            margin-bottom: 20px;
        }
        
        .search-input {
            width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 8px;
            font-size: 16px; font-family: inherit; margin-bottom: 10px;
        }
        
        .button-row {
            display: flex; gap: 10px;
        }
        
        .search-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border: none; padding: 12px 20px; border-radius: 8px; 
            cursor: pointer; font-size: 16px; font-weight: 600; transition: transform 0.2s;
            white-space: nowrap; flex: 1;
        }
        .search-btn:hover { transform: translateY(-2px); }
        .search-btn:disabled { background: #ccc; cursor: not-allowed; transform: none; }
        
        .clear-btn {
            background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
            color: white; border: none; padding: 12px 20px; border-radius: 8px; 
            cursor: pointer; font-size: 16px; font-weight: 600; transition: transform 0.2s;
            white-space: nowrap; flex: 1;
        }
        .clear-btn:hover {
            background: linear-gradient(135deg, #545b62 0%, #343a40 100%);
            transform: translateY(-2px);
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
        
        /* Desktop tabs */
        .desktop-tabs {
            display: flex;
            background: white;
            border-bottom: 1px solid #e1e5e9;
            flex-shrink: 0;
        }
        
        .desktop-tab-button {
            padding: 15px 30px;
            background: transparent;
            border: none;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            color: #666;
            transition: all 0.2s;
            border-bottom: 3px solid transparent;
        }
        
        .desktop-tab-button.active {
            color: #007bff;
            border-bottom-color: #007bff;
            background: #f8f9fa;
        }
        
        .desktop-tab-button:hover {
            background: #f8f9fa;
        }
        
        .desktop-tab-content {
            display: none;
            flex: 1;
            overflow: hidden;
            flex-direction: column;
        }
        
        .desktop-tab-content.active {
            display: flex;
        }
        
        /* Tab layout styles */
        .tab-container {
            display: none;
            flex-direction: column;
            height: 100vh;
        }
        
        .tab-header {
            display: flex;
            background: white;
            border-bottom: 1px solid #e1e5e9;
            flex-shrink: 0;
        }
        
        .tab-button {
            flex: 1;
            padding: 15px 20px;
            background: transparent;
            border: none;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            color: #666;
            transition: all 0.2s;
            border-bottom: 3px solid transparent;
        }
        
        .tab-button.active {
            color: #007bff;
            border-bottom-color: #007bff;
            background: #f8f9fa;
        }
        
        .tab-button:hover {
            background: #f8f9fa;
        }
        
        .tab-content {
            flex: 1;
            overflow: hidden;
            display: none;
        }
        
        .tab-content.active {
            display: flex;
            flex-direction: column;
        }
        
        /* Compatibility Checker Styles */
        .compatibility-section {
            padding: 20px;
            flex: 1;
            overflow-y: auto;
        }
        
        .compatibility-result {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #e1e5e9;
        }
        
        .compatibility-result.yay {
            background: #d4edda;
            border-color: #c3e6cb;
            color: #155724;
        }
        
        .compatibility-result.nay {
            background: #f8d7da;
            border-color: #f5c6cb;
            color: #721c24;
        }
        
        .compatibility-result .decision {
            font-size: 1.5em;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .compatibility-result .reason {
            font-size: 1em;
            line-height: 1.5;
            margin-bottom: 15px;
        }
        
        .compatibility-result .details {
            margin-top: 15px;
            font-size: 0.9em;
        }
        
        .compatibility-result .details h4 {
            margin-bottom: 10px;
            font-size: 1em;
        }
        
        .compatibility-result .details ul {
            margin-left: 20px;
            margin-top: 5px;
        }
        
        .compatibility-result .details li {
            margin-bottom: 5px;
        }
        
        /* Loading message styles */
        .loading-message {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #666;
            font-style: italic;
        }
        
        .loading-message::after {
            content: '';
            width: 16px;
            height: 16px;
            border: 2px solid #f3f3f3;
            border-top: 2px solid #007bff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        /* Responsive breakpoints */
        @media (max-width: 1280px) {
            /* No changes needed - layout is already optimal */
        }
        
        @media (max-width: 768px) {
            .desktop-tabs {
                display: none;
            }
            
            .desktop-tab-content {
                display: none !important;
            }
            
            .main-container {
                display: none;
            }
            
            .tab-container {
                display: flex;
            }
            
            .left-panel, .right-panel {
                width: 100%;
                height: 100%;
            }
            
            .panel-header {
                display: none;
            }
            
            .code-search-section {
                padding: 15px;
            }
            
            .chat-container {
                height: 100%;
            }
            
            .chat-messages {
                padding: 15px;
            }
            
            .chat-input-container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <!-- Desktop Layout -->
    <div class="desktop-tabs">
        <button class="desktop-tab-button active" onclick="switchDesktopTab('main')">
            💬 Chat & Lookup
        </button>
        <button class="desktop-tab-button" onclick="switchDesktopTab('compatibility')">
            ✅ Compatibility Check
        </button>
    </div>
    
    <div class="desktop-tab-content active" id="desktop-main-tab">
        <div class="main-container">
        <!-- Left Panel: Code Number Search -->
        <div class="left-panel">
            <div class="panel-header">
                📋 MBS Code Lookup
            </div>
            <div class="code-search-section">
                <div class="input-group">
                    <label for="codes">Enter MBS item numbers (comma-separated):</label>
                </div>
                
                <div class="search-container">
                    <input type="text" id="codes" class="search-input" placeholder="e.g., 3,23,104" />
                    <div class="button-row">
                        <button class="search-btn" onclick="performCodeSearch()">🔍 Lookup</button>
                        <button class="clear-btn" onclick="clearCodeSearch()">🗑️ Clear</button>
                    </div>
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
                <span id="ai-status-header" class="ai-status-header">
                    <div class="loading">Checking AI services...</div>
                </span>
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
    </div>
    
    <div class="desktop-tab-content" id="desktop-compatibility-tab">
        <div class="compatibility-section" style="width: 100%; max-width: 1200px; margin: 0 auto;">
            <div class="panel-header">
                ✅ MBS Code Compatibility Checker
            </div>
            <div style="padding: 20px;">
                <div class="input-group">
                    <label for="desktop-compatibility-codes">Enter MBS item numbers to check compatibility (comma-separated):</label>
                </div>
                
                <div class="search-container">
                    <input type="text" id="desktop-compatibility-codes" class="search-input" placeholder="e.g., 3,23,104" />
                    <div class="button-row">
                        <button class="search-btn" onclick="performDesktopCompatibilityCheck()">✅ Check Compatibility</button>
                        <button class="clear-btn" onclick="clearDesktopCompatibilityCheck()">🗑️ Clear</button>
                    </div>
                </div>
                
                <div id="desktop-compatibility-error" class="error" style="display: none;"></div>
                <div id="desktop-compatibility-notice" class="notice" style="display: none;"></div>
                
                <div id="desktop-compatibility-results" class="results"></div>
            </div>
        </div>
    </div>
    
    <!-- Mobile Tab Layout -->
    <div class="tab-container">
        <div class="tab-header">
            <button class="tab-button active" onclick="switchTab('chat')">
                💬 AI Assistant Chat
                <span id="mobile-ai-status" class="ai-status-header" style="font-size: 0.8em;">
                    <div class="loading">Checking...</div>
                </span>
            </button>
            <button class="tab-button" onclick="switchTab('lookup')">
                📋 MBS Code Lookup
            </button>
            <button class="tab-button" onclick="switchTab('compatibility')">
                ✅ Compatibility Check
            </button>
        </div>
        
        <div class="tab-content active" id="chat-tab">
            <div class="right-panel">
                <div class="chat-container">
                    <div class="chat-messages" id="mobile-chat-messages">
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
                                id="mobile-chat-input" 
                                class="chat-input" 
                                placeholder="Describe the medical procedure or consultation..."
                                rows="1"
                            ></textarea>
                            <button id="mobile-chat-send-btn" class="chat-send-btn" onclick="sendMobileMessage()">
                                ➤
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="tab-content" id="lookup-tab">
            <div class="left-panel">
                <div class="code-search-section">
                    <div class="input-group">
                        <label for="mobile-codes">Enter MBS item numbers (comma-separated):</label>
                    </div>
                    
                    <div class="search-container">
                        <input type="text" id="mobile-codes" class="search-input" placeholder="e.g., 3,23,104" />
                        <div class="button-row">
                            <button class="search-btn" onclick="performMobileCodeSearch()">🔍 Lookup</button>
                            <button class="clear-btn" onclick="clearMobileCodeSearch()">🗑️ Clear</button>
                        </div>
                    </div>
                    
                    <div id="mobile-code-search-error" class="error" style="display: none;"></div>
                    <div id="mobile-code-search-notice" class="notice" style="display: none;"></div>
                    
                    <div id="mobile-code-search-results" class="results"></div>
                </div>
            </div>
        </div>
        
        <div class="tab-content" id="compatibility-tab">
            <div class="compatibility-section">
                <div class="input-group">
                    <label for="mobile-compatibility-codes">Enter MBS item numbers to check compatibility (comma-separated):</label>
                </div>
                
                <div class="search-container">
                    <input type="text" id="mobile-compatibility-codes" class="search-input" placeholder="e.g., 3,23,104" />
                    <div class="button-row">
                        <button class="search-btn" onclick="performMobileCompatibilityCheck()">✅ Check Compatibility</button>
                        <button class="clear-btn" onclick="clearMobileCompatibilityCheck()">🗑️ Clear</button>
                    </div>
                </div>
                
                <div id="mobile-compatibility-error" class="error" style="display: none;"></div>
                <div id="mobile-compatibility-notice" class="notice" style="display: none;"></div>
                
                <div id="mobile-compatibility-results" class="results"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Global variables
        let aiEnabled = false;
        let conversationHistory = [];
        let isProcessing = false;
        let mobileConversationHistory = [];
        let isMobileProcessing = false;
        
        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            checkAIStatus();
            setupEventListeners();
            setupMobileEventListeners();
        });
        
        function setupEventListeners() {
            const chatInput = document.getElementById('chat-input');
            const chatSendBtn = document.getElementById('chat-send-btn');
            
            // Auto-resize textarea and adjust padding
            chatInput.addEventListener('input', function() {
                this.style.height = 'auto';
                const maxHeight = window.innerHeight * 0.25; // 25% of viewport height
                this.style.height = Math.min(this.scrollHeight, maxHeight) + 'px';
                
                // Adjust padding based on content
                if (this.value.trim() === '') {
                    this.style.padding = '2px 6px';
                } else {
                    this.style.padding = '14px 6px';
                }
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
            
            // Desktop compatibility input Enter key
            document.getElementById('desktop-compatibility-codes').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    performDesktopCompatibilityCheck();
                }
            });
        }
        
        async function checkAIStatus() {
            try {
                const response = await fetch('/api/ai/status');
                const data = await response.json();
                
                aiEnabled = data.ai_enabled;
                
                // Update desktop status
                const statusElement = document.getElementById('ai-status-header');
                if (aiEnabled) {
                    statusElement.innerHTML = '✅ Ready';
                } else {
                    statusElement.innerHTML = '❌ Unavailable';
                }
                
                // Update mobile status
                const mobileStatusElement = document.getElementById('mobile-ai-status');
                if (aiEnabled) {
                    mobileStatusElement.innerHTML = '';
                } else {
                    mobileStatusElement.innerHTML = '❌ Unavailable';
                }
            } catch (error) {
                const statusElement = document.getElementById('ai-status-header');
                statusElement.innerHTML = '❌ Error';
                
                const mobileStatusElement = document.getElementById('mobile-ai-status');
                mobileStatusElement.innerHTML = '❌ Error';
            }
        }
        
        async function sendMessage() {
            const chatInput = document.getElementById('chat-input');
            const message = chatInput.value.trim();
            
            if (!message || isProcessing) return;
            
            // Clear input
            chatInput.value = '';
            chatInput.style.height = 'auto';
            chatInput.style.padding = '2px 6px';
            
            // Add user message to chat
            addMessageToChat('user', message);
            
            // Add loading message
            addLoadingMessageToChat();
            
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
                
                // Remove loading message
                removeLoadingMessageFromChat();
                
                if (data.error) {
                    // Handle error response
                    addMessageToChat('assistant', `❌ ${data.error}`);
                } else if (data.suggested_codes && data.suggested_codes.length > 0) {
                    // Handle successful response with suggestions
                    const responseText = `I found ${data.suggested_codes.length} MBS codes that match your description:`;
                    addMessageToChat('assistant', responseText);
                    
                    // Add suggestions - check if detailed_suggestions exist, otherwise use suggested_codes
                    if (data.detailed_suggestions && data.detailed_suggestions.length > 0) {
                        addSuggestionsToChat(data.detailed_suggestions);
                    }

                    // Add suggested codes as clickable buttons
                    if (data.suggested_codes && data.suggested_codes.length > 0) {
                        // Display suggested codes as clickable buttons
                        addSimpleSuggestionsToChat(data.suggested_codes);
                    }
                    
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
                // Remove loading message on error
                removeLoadingMessageFromChat();
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
        
        function addLoadingMessageToChat() {
            const chatMessages = document.getElementById('chat-messages');
            
            // Remove empty state if it exists
            const emptyState = chatMessages.querySelector('.empty-state');
            if (emptyState) {
                emptyState.remove();
            }
            
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'message assistant';
            loadingDiv.id = 'loading-message';
            
            loadingDiv.innerHTML = `
                <div class="message-content">
                    <div class="loading-message">Thinking...</div>
                </div>
            `;
            
            chatMessages.appendChild(loadingDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function removeLoadingMessageFromChat() {
            const loadingMessage = document.getElementById('loading-message');
            if (loadingMessage) {
                loadingMessage.remove();
            }
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
        
        function addSimpleSuggestionsToChat(suggestedCodes) {
            const chatMessages = document.getElementById('chat-messages');
            
            const suggestionsDiv = document.createElement('div');
            suggestionsDiv.className = 'message assistant';
            
            let html = '<div class="message-content"><div class="ai-suggestions">';
            html += '<p style="margin-bottom: 15px; color: #666;">Click on any code below to add it to the lookup panel:</p>';
            
            // Create a grid of clickable code buttons
            html += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px;">';
            
            suggestedCodes.forEach(code => {
                html += `
                    <button class="btn" style="margin: 0; padding: 10px 15px; font-size: 14px;" onclick="addCodeToLeftPanel('${code}')">
                        ${code}
                    </button>
                `;
            });
            
            html += '</div></div></div>';
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
            const maxHeight = window.innerHeight * 0.25; // 25% of viewport height
            chatInput.style.height = Math.min(chatInput.scrollHeight, maxHeight) + 'px';
            chatInput.style.padding = '14px 6px';
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
        
        // Code search functionality
        async function performCodeSearch() {
            const codesInput = document.getElementById('codes').value.trim();
            if (!codesInput) {
                showError('code-search-error', 'Please enter one or more MBS item numbers.');
                return Promise.resolve();
            }
            
            const codes = codesInput.split(',').map(c => c.trim()).filter(c => c);
            if (codes.length === 0) {
                showError('code-search-error', 'Please enter valid MBS item numbers.');
                return Promise.resolve();
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
                
                return Promise.resolve();
                
            } catch (error) {
                showError('code-search-error', 'Lookup failed: ' + error.message);
                return Promise.resolve();
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
                performCodeSearch().then(() => {
                    // Scroll to the newly added code element after search completes
                    setTimeout(() => {
                        scrollToCodeElement(code);
                    }, 100);
                });
            } else {
                // If code already exists, just scroll to it
                scrollToCodeElement(code);
            }
        }
        
        function scrollToCodeElement(code) {
            const codeElement = document.querySelector(`[data-item-code="${code}"]`);
            if (codeElement) {
                codeElement.scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'center',
                    inline: 'nearest'
                });
                
                // Add a temporary highlight effect
                codeElement.style.backgroundColor = '#fff3cd';
                codeElement.style.borderColor = '#ffc107';
                setTimeout(() => {
                    codeElement.style.backgroundColor = '';
                    codeElement.style.borderColor = '';
                }, 2000);
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
        
        // Mobile functionality
        function setupMobileEventListeners() {
            const mobileChatInput = document.getElementById('mobile-chat-input');
            const mobileChatSendBtn = document.getElementById('mobile-chat-send-btn');
            
            // Auto-resize textarea and adjust padding
            mobileChatInput.addEventListener('input', function() {
                this.style.height = 'auto';
                const maxHeight = window.innerHeight * 0.25; // 25% of viewport height
                this.style.height = Math.min(this.scrollHeight, maxHeight) + 'px';
                
                // Adjust padding based on content
                if (this.value.trim() === '') {
                    this.style.padding = '2px 6px';
                } else {
                    this.style.padding = '14px 6px';
                }
            });
            
            // Send message on Enter (but not Shift+Enter)
            mobileChatInput.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    sendMobileMessage();
                }
            });
            
            // Send button click
            mobileChatSendBtn.addEventListener('click', sendMobileMessage);
            
            // Mobile code input Enter key
            document.getElementById('mobile-codes').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    performMobileCodeSearch();
                }
            });
            
            // Mobile compatibility input Enter key
            document.getElementById('mobile-compatibility-codes').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    performMobileCompatibilityCheck();
                }
            });
        }
        
        function switchTab(tabName) {
            // Remove active class from all tabs and buttons
            document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            // Add active class to selected tab and button
            document.querySelector(`[onclick="switchTab('${tabName}')"]`).classList.add('active');
            document.getElementById(`${tabName}-tab`).classList.add('active');
        }
        
        function switchDesktopTab(tabName) {
            // Remove active class from all desktop tabs and content
            document.querySelectorAll('.desktop-tab-button').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.desktop-tab-content').forEach(content => content.classList.remove('active'));
            
            // Add active class to selected tab and content
            document.querySelector(`[onclick="switchDesktopTab('${tabName}')"]`).classList.add('active');
            document.getElementById(`desktop-${tabName}-tab`).classList.add('active');
        }
        
        async function sendMobileMessage() {
            const chatInput = document.getElementById('mobile-chat-input');
            const message = chatInput.value.trim();
            
            if (!message || isMobileProcessing) return;
            
            // Clear input
            chatInput.value = '';
            chatInput.style.height = 'auto';
            chatInput.style.padding = '2px 6px';
            
            // Add user message to mobile chat
            addMessageToMobileChat('user', message);
            
            // Add loading message
            addLoadingMessageToMobileChat();
            
            // Show processing state
            setMobileProcessingState(true);
            
            try {
                let response;
                
                if (mobileConversationHistory.length > 0) {
                    // Use conversational endpoint
                    response = await fetch('/api/ai/conversation', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ 
                            query: message,
                            conversation_history: mobileConversationHistory
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
                
                // Add to mobile conversation history
                mobileConversationHistory.push({
                    type: 'user',
                    content: message,
                    timestamp: new Date().toISOString()
                });
                
                // Remove loading message
                removeLoadingMessageFromMobileChat();
                
                if (data.error) {
                    // Handle error response
                    addMessageToMobileChat('assistant', `❌ ${data.error}`);
                } else if (data.suggested_codes && data.suggested_codes.length > 0) {
                    // Handle successful response with suggestions
                    const responseText = `I found ${data.suggested_codes.length} MBS codes that match your description:`;
                    addMessageToMobileChat('assistant', responseText);
                    
                    // Add suggestions - check if detailed_suggestions exist, otherwise use suggested_codes
                    if (data.detailed_suggestions && data.detailed_suggestions.length > 0) {
                        addSuggestionsToMobileChat(data.detailed_suggestions);
                    }

                    // Add suggested codes as clickable buttons
                    if (data.suggested_codes && data.suggested_codes.length > 0) {
                        // Display suggested codes as clickable buttons
                        addSimpleSuggestionsToMobileChat(data.suggested_codes);
                    }
                    
                    // Add follow-up prompts
                    if (data.follow_up_questions && data.follow_up_questions.length > 0) {
                        addFollowUpPromptsToMobileChat(data.follow_up_questions);
                    }
                    
                    // Add assistant response to mobile conversation history
                    mobileConversationHistory.push({
                        type: 'assistant',
                        content: responseText,
                        suggested_codes: data.suggested_codes,
                        timestamp: new Date().toISOString()
                    });
                } else {
                    // No suggestions found
                    addMessageToMobileChat('assistant', "I couldn't find any matching MBS codes for that description. Could you provide more details about the procedure or consultation?");
                }
                
            } catch (error) {
                // Remove loading message on error
                removeLoadingMessageFromMobileChat();
                addMessageToMobileChat('assistant', `❌ Sorry, there was an error processing your request: ${error.message}`);
            } finally {
                setMobileProcessingState(false);
            }
        }
        
        function addMessageToMobileChat(type, content) {
            const chatMessages = document.getElementById('mobile-chat-messages');
            
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
        
        function addLoadingMessageToMobileChat() {
            const chatMessages = document.getElementById('mobile-chat-messages');
            
            // Remove empty state if it exists
            const emptyState = chatMessages.querySelector('.empty-state');
            if (emptyState) {
                emptyState.remove();
            }
            
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'message assistant';
            loadingDiv.id = 'mobile-loading-message';
            
            loadingDiv.innerHTML = `
                <div class="message-content">
                    <div class="loading-message">Thinking...</div>
                </div>
            `;
            
            chatMessages.appendChild(loadingDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function removeLoadingMessageFromMobileChat() {
            const loadingMessage = document.getElementById('mobile-loading-message');
            if (loadingMessage) {
                loadingMessage.remove();
            }
        }
        
        function setMobileProcessingState(processing) {
            isMobileProcessing = processing;
            const sendBtn = document.getElementById('mobile-chat-send-btn');
            const chatInput = document.getElementById('mobile-chat-input');
            
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
        
        // Mobile code search functionality
        async function performMobileCodeSearch() {
            const codesInput = document.getElementById('mobile-codes').value.trim();
            if (!codesInput) {
                showError('mobile-code-search-error', 'Please enter one or more MBS item numbers.');
                return Promise.resolve();
            }
            
            const codes = codesInput.split(',').map(c => c.trim()).filter(c => c);
            if (codes.length === 0) {
                showError('mobile-code-search-error', 'Please enter valid MBS item numbers.');
                return Promise.resolve();
            }
            
            showLoading('mobile-code-search-notice', 'Looking up MBS codes...');
            
            try {
                const response = await fetch('/api/items?codes=' + encodeURIComponent(codes.join(',')));
                const data = await response.json();
                
                if (data.items && data.items.length > 0) {
                    displayMobileResults(data.items);
                    showSuccess('mobile-code-search-notice', `Found ${data.items.length} MBS codes`);
                } else {
                    showNotice('mobile-code-search-notice', 'No codes found. Please check the item numbers.');
                }
                
                return Promise.resolve();
                
            } catch (error) {
                showError('mobile-code-search-error', 'Lookup failed: ' + error.message);
                return Promise.resolve();
            } finally {
                hideLoading('mobile-code-search-notice');
            }
        }
        
        function clearMobileCodeSearch() {
            document.getElementById('mobile-codes').value = '';
            document.getElementById('mobile-code-search-results').innerHTML = '';
            hideMessages(['mobile-code-search-error', 'mobile-code-search-notice']);
        }
        
        function addCodeToMobileLeftPanel(code) {
            const inputField = document.getElementById('mobile-codes');
            const currentCodes = inputField.value ? inputField.value.split(',').map(c => c.trim()) : [];
            
            if (!currentCodes.includes(code)) {
                currentCodes.push(code);
                inputField.value = currentCodes.join(', ');
                performMobileCodeSearch().then(() => {
                    // Scroll to the newly added code element after search completes
                    setTimeout(() => {
                        scrollToMobileCodeElement(code);
                    }, 100);
                });
            } else {
                // If code already exists, just scroll to it
                scrollToMobileCodeElement(code);
            }
        }
        
        function scrollToMobileCodeElement(code) {
            const codeElement = document.querySelector(`[data-mobile-item-code="${code}"]`);
            if (codeElement) {
                codeElement.scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'center',
                    inline: 'nearest'
                });
                
                // Add a temporary highlight effect
                codeElement.style.backgroundColor = '#fff3cd';
                codeElement.style.borderColor = '#ffc107';
                setTimeout(() => {
                    codeElement.style.backgroundColor = '';
                    codeElement.style.borderColor = '';
                }, 2000);
            }
        }
        
        function displayMobileResults(items) {
            const container = document.getElementById('mobile-code-search-results');
            if (!items || items.length === 0) {
                container.innerHTML = '';
                return;
            }
            
            let html = '<h3>📋 MBS Code Results</h3>';
            
            items.forEach(item => {
                html += `
                    <div class="item" data-mobile-item-code="${item.item.item_num}">
                        <div class="item-header">
                            <span class="item-title">MBS Code ${item.item.item_num}</span>
                            <button class="remove-btn" onclick="removeMobileItem('${item.item.item_num}')">✕</button>
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
                                        ${rel.target_item_num ? `<span class="clickable-code" onclick="addCodeToMobileLeftPanel('${rel.target_item_num}')">${rel.target_item_num}</span>` : ''}
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
        
        function removeMobileItem(itemCode) {
            const itemElement = document.querySelector(`[data-mobile-item-code="${itemCode}"]`);
            if (itemElement) {
                itemElement.remove();
                updateMobileLeftPanelInputField();
            }
        }
        
        function updateMobileLeftPanelInputField() {
            const displayedItems = document.querySelectorAll('#mobile-code-search-results .item');
            const codes = [];
            displayedItems.forEach(item => {
                const code = item.getAttribute('data-mobile-item-code');
                if (code) {
                    codes.push(code);
                }
            });
            
            const inputField = document.getElementById('mobile-codes');
            inputField.value = codes.join(', ');
        }
        
        // Mobile suggestion functions
        function addSuggestionsToMobileChat(suggestions) {
            const chatMessages = document.getElementById('mobile-chat-messages');
            
            const suggestionsDiv = document.createElement('div');
            suggestionsDiv.className = 'message assistant';
            
            let html = '<div class="message-content"><div class="ai-suggestions">';
            
            suggestions.forEach(suggestion => {
                html += `
                    <div class="suggestion">
                        <div class="suggestion-header">
                            <span class="suggestion-code clickable-code" onclick="addCodeToMobileLeftPanel('${suggestion.code}')">
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
        
        function addSimpleSuggestionsToMobileChat(suggestedCodes) {
            const chatMessages = document.getElementById('mobile-chat-messages');
            
            const suggestionsDiv = document.createElement('div');
            suggestionsDiv.className = 'message assistant';
            
            let html = '<div class="message-content"><div class="ai-suggestions">';
            html += '<p style="margin-bottom: 15px; color: #666;">Click on any code below to add it to the lookup panel:</p>';
            
            // Create a grid of clickable code buttons
            html += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px;">';
            
            suggestedCodes.forEach(code => {
                html += `
                    <button class="btn" style="margin: 0; padding: 10px 15px; font-size: 14px;" onclick="addCodeToMobileLeftPanel('${code}')">
                        ${code}
                    </button>
                `;
            });
            
            html += '</div></div></div>';
            suggestionsDiv.innerHTML = html;
            
            chatMessages.appendChild(suggestionsDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function addFollowUpPromptsToMobileChat(questions) {
            const chatMessages = document.getElementById('mobile-chat-messages');
            
            const promptsDiv = document.createElement('div');
            promptsDiv.className = 'message assistant';
            
            let html = `
                <div class="message-content">
                    <div class="follow-up-prompt">
                        <h4>💡 To help me find more specific codes, please provide:</h4>
            `;
            
            questions.forEach(question => {
                html += `
                    <div class="follow-up-suggestion" onclick="useMobileFollowUpPrompt('${question.replace(/'/g, "\\'")}')">
                        ${question}
                    </div>
                `;
            });
            
            html += '</div></div>';
            promptsDiv.innerHTML = html;
            
            chatMessages.appendChild(promptsDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function useMobileFollowUpPrompt(question) {
            const chatInput = document.getElementById('mobile-chat-input');
            chatInput.value = question;
            chatInput.focus();
            chatInput.style.height = 'auto';
            const maxHeight = window.innerHeight * 0.25; // 25% of viewport height
            chatInput.style.height = Math.min(chatInput.scrollHeight, maxHeight) + 'px';
            chatInput.style.padding = '14px 6px';
        }
        
        // Mobile Compatibility Checker Functions
        async function performMobileCompatibilityCheck() {
            const codesInput = document.getElementById('mobile-compatibility-codes').value.trim();
            if (!codesInput) {
                showError('mobile-compatibility-error', 'Please enter one or more MBS item numbers.');
                return;
            }
            
            const codes = codesInput.split(',').map(c => c.trim()).filter(c => c);
            if (codes.length === 0) {
                showError('mobile-compatibility-error', 'Please enter valid MBS item numbers.');
                return;
            }
            
            showLoading('mobile-compatibility-notice', 'Checking compatibility...');
            hideMessages(['mobile-compatibility-error']);
            
            try {
                const response = await fetch('/api/compatibility/check', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ codes: codes })
                });
                
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.detail || 'Compatibility check failed');
                }
                
                displayMobileCompatibilityResult(data);
                hideLoading('mobile-compatibility-notice');
                
            } catch (error) {
                showError('mobile-compatibility-error', 'Compatibility check failed: ' + error.message);
                hideLoading('mobile-compatibility-notice');
            }
        }
        
        function displayMobileCompatibilityResult(result) {
            const container = document.getElementById('mobile-compatibility-results');
            
            const decisionClass = result.decision === 'YAY' ? 'yay' : 'nay';
            const decisionEmoji = result.decision === 'YAY' ? '✅' : '❌';
            
            let html = `
                <div class="compatibility-result ${decisionClass}">
                    <div class="decision">${decisionEmoji} ${result.decision}</div>
                    <div class="reason">${result.reason}</div>
            `;
            
            if (result.details) {
                html += '<div class="details">';
                
                if (result.details.invalid_codes && result.details.invalid_codes.length > 0) {
                    html += '<h4>Invalid Codes:</h4><ul>';
                    result.details.invalid_codes.forEach(code => {
                        html += `<li>${code}</li>`;
                    });
                    html += '</ul>';
                }
                
                if (result.details.violations && result.details.violations.length > 0) {
                    html += '<h4>Violations:</h4><ul>';
                    result.details.violations.forEach(violation => {
                        if (violation.code1 && violation.code2) {
                            html += `<li>${violation.code1} and ${violation.code2}: ${violation.detail || violation.type}</li>`;
                        } else if (violation.code) {
                            html += `<li>Code ${violation.code}: ${violation.limit || 'Duplicate violation'} (submitted ${violation.count} times)</li>`;
                        }
                    });
                    html += '</ul>';
                }
                
                if (result.details.missing_dependencies && result.details.missing_dependencies.length > 0) {
                    html += '<h4>Missing Dependencies:</h4><ul>';
                    result.details.missing_dependencies.forEach(dep => {
                        html += `<li>Code ${dep.code} requires ${dep.required_code}: ${dep.detail || 'Prerequisite missing'}</li>`;
                    });
                    html += '</ul>';
                }
                
                if (result.details.solo_codes && result.details.solo_codes.length > 0) {
                    html += '<h4>Solo-Only Codes:</h4><ul>';
                    result.details.solo_codes.forEach(code => {
                        html += `<li>Code ${code} must be billed alone</li>`;
                    });
                    html += '</ul>';
                }
                
                html += '</div>';
            }
            
            html += '</div>';
            container.innerHTML = html;
        }
        
        function clearMobileCompatibilityCheck() {
            document.getElementById('mobile-compatibility-codes').value = '';
            document.getElementById('mobile-compatibility-results').innerHTML = '';
            hideMessages(['mobile-compatibility-error', 'mobile-compatibility-notice']);
        }
        
        // Desktop Compatibility Checker Functions
        async function performDesktopCompatibilityCheck() {
            const codesInput = document.getElementById('desktop-compatibility-codes').value.trim();
            if (!codesInput) {
                showError('desktop-compatibility-error', 'Please enter one or more MBS item numbers.');
                return;
            }
            
            const codes = codesInput.split(',').map(c => c.trim()).filter(c => c);
            if (codes.length === 0) {
                showError('desktop-compatibility-error', 'Please enter valid MBS item numbers.');
                return;
            }
            
            showLoading('desktop-compatibility-notice', 'Checking compatibility...');
            hideMessages(['desktop-compatibility-error']);
            
            try {
                const response = await fetch('/api/compatibility/check', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ codes: codes })
                });
                
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.detail || 'Compatibility check failed');
                }
                
                displayDesktopCompatibilityResult(data);
                hideLoading('desktop-compatibility-notice');
                
            } catch (error) {
                showError('desktop-compatibility-error', 'Compatibility check failed: ' + error.message);
                hideLoading('desktop-compatibility-notice');
            }
        }
        
        function displayDesktopCompatibilityResult(result) {
            const container = document.getElementById('desktop-compatibility-results');
            
            const decisionClass = result.decision === 'YAY' ? 'yay' : 'nay';
            const decisionEmoji = result.decision === 'YAY' ? '✅' : '❌';
            
            let html = `
                <div class="compatibility-result ${decisionClass}">
                    <div class="decision">${decisionEmoji} ${result.decision}</div>
                    <div class="reason">${result.reason}</div>
            `;
            
            if (result.details) {
                html += '<div class="details">';
                
                if (result.details.invalid_codes && result.details.invalid_codes.length > 0) {
                    html += '<h4>Invalid Codes:</h4><ul>';
                    result.details.invalid_codes.forEach(code => {
                        html += `<li>${code}</li>`;
                    });
                    html += '</ul>';
                }
                
                if (result.details.violations && result.details.violations.length > 0) {
                    html += '<h4>Violations:</h4><ul>';
                    result.details.violations.forEach(violation => {
                        if (violation.code1 && violation.code2) {
                            html += `<li>${violation.code1} and ${violation.code2}: ${violation.detail || violation.type}</li>`;
                        } else if (violation.code) {
                            html += `<li>Code ${violation.code}: ${violation.limit || 'Duplicate violation'} (submitted ${violation.count} times)</li>`;
                        }
                    });
                    html += '</ul>';
                }
                
                if (result.details.missing_dependencies && result.details.missing_dependencies.length > 0) {
                    html += '<h4>Missing Dependencies:</h4><ul>';
                    result.details.missing_dependencies.forEach(dep => {
                        html += `<li>Code ${dep.code} requires ${dep.required_code}: ${dep.detail || 'Prerequisite missing'}</li>`;
                    });
                    html += '</ul>';
                }
                
                if (result.details.solo_codes && result.details.solo_codes.length > 0) {
                    html += '<h4>Solo-Only Codes:</h4><ul>';
                    result.details.solo_codes.forEach(code => {
                        html += `<li>Code ${code} must be billed alone</li>`;
                    });
                    html += '</ul>';
                }
                
                html += '</div>';
            }
            
            html += '</div>';
            container.innerHTML = html;
        }
        
        function clearDesktopCompatibilityCheck() {
            document.getElementById('desktop-compatibility-codes').value = '';
            document.getElementById('desktop-compatibility-results').innerHTML = '';
            hideMessages(['desktop-compatibility-error', 'desktop-compatibility-notice']);
        }
    </script>
</body>
</html>
"""
