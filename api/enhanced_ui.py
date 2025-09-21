"""
Enhanced HTML interface for MBS Clarity AI assistant.

This module provides an enhanced HTML interface with AI-powered features including
natural language search, contextual chatbot, and smart code suggestions.
"""

ENHANCED_HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>MBS Clarity AI Assistant</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; background: #f5f5f5; }
    .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
    .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; text-align: center; }
    .header h1 { font-size: 2.5em; margin-bottom: 10px; }
    .header p { font-size: 1.2em; opacity: 0.9; }
    
    .main-content { display: grid; grid-template-columns: 1fr 400px; gap: 30px; }
    
    .search-section { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .search-section h2 { margin-bottom: 20px; color: #333; }
    
    .input-group { margin-bottom: 20px; }
    .input-group label { display: block; margin-bottom: 8px; font-weight: 600; color: #555; }
    .input-group input, .input-group textarea { width: 100%; padding: 12px; border: 2px solid #e1e5e9; border-radius: 8px; font-size: 16px; transition: border-color 0.3s; }
    .input-group input:focus, .input-group textarea:focus { outline: none; border-color: #667eea; }
    .input-group textarea { resize: vertical; min-height: 100px; }
    
    .search-tabs { display: flex; margin-bottom: 20px; border-bottom: 2px solid #e1e5e9; }
    .search-tab { padding: 12px 20px; background: none; border: none; cursor: pointer; font-size: 16px; color: #666; border-bottom: 3px solid transparent; transition: all 0.3s; }
    .search-tab.active { color: #667eea; border-bottom-color: #667eea; font-weight: 600; }
    .search-tab:hover { color: #667eea; }
    
    .search-content { display: none; }
    .search-content.active { display: block; }
    
    .btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: 600; transition: transform 0.2s; }
    .btn:hover { transform: translateY(-2px); }
    .btn:disabled { background: #ccc; cursor: not-allowed; transform: none; }
    .btn-secondary { background: #6c757d; }
    .btn-success { background: #28a745; }
    .btn-danger { background: #dc3545; }
    
    .results { margin-top: 30px; }
    .results h3 { margin-bottom: 20px; color: #333; }
    
    .item { background: white; border: 1px solid #e1e5e9; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); transition: box-shadow 0.3s; }
    .item:hover { box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    
    .item-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
    .item-title { font-size: 1.5em; font-weight: 700; color: #667eea; }
    .remove-btn { background: #ff4444; color: white; border: none; border-radius: 50%; width: 30px; height: 30px; cursor: pointer; font-size: 16px; font-weight: bold; display: flex; align-items: center; justify-content: center; line-height: 1; }
    .remove-btn:hover { background: #cc0000; }
    
    .item-details { margin-bottom: 15px; }
    .item-detail { margin-bottom: 8px; }
    .item-detail strong { color: #555; }
    
    .constraints { margin-top: 15px; }
    .constraint-group { margin-bottom: 15px; }
    .constraint-group h4 { color: #667eea; margin-bottom: 8px; font-size: 1.1em; }
    .constraint-list { list-style: none; }
    .constraint-list li { background: #f8f9fa; padding: 8px 12px; margin-bottom: 5px; border-radius: 5px; border-left: 4px solid #667eea; }
    
    .relations { margin-top: 15px; }
    .relation { background: #e3f2fd; padding: 8px 12px; margin-bottom: 5px; border-radius: 5px; border-left: 4px solid #2196f3; }
    .clickable-code { cursor: pointer; background: #e3f2fd; border: 1px solid #2196f3; padding: 2px 6px; border-radius: 3px; margin: 0 2px; }
    .clickable-code:hover { background: #bbdefb; }
    
    .ai-suggestions { margin-top: 20px; }
    .suggestion { background: #f0f8ff; border: 1px solid #b3d9ff; border-radius: 8px; padding: 15px; margin-bottom: 15px; }
    .suggestion-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
    .suggestion-code { font-size: 1.2em; font-weight: 700; color: #0066cc; }
    .suggestion-confidence { background: #28a745; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; }
    .suggestion-reasoning { color: #666; font-style: italic; margin-bottom: 10px; }
    .suggestion-requirements { margin-bottom: 10px; }
    .suggestion-requirements h5 { color: #333; margin-bottom: 5px; }
    .suggestion-requirements ul { margin-left: 20px; }
    
    .follow-up-questions { margin-top: 20px; }
    .follow-up-question { background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 5px; padding: 10px; margin-bottom: 10px; cursor: pointer; transition: background-color 0.3s; }
    .follow-up-question:hover { background: #ffeaa7; }
    
    .chatbot { background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); height: 600px; display: flex; flex-direction: column; }
    .chatbot-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px 10px 0 0; text-align: center; }
    .chatbot-header h3 { margin: 0; }
    
    .chatbot-messages { flex: 1; padding: 20px; overflow-y: auto; max-height: 400px; }
    .chatbot-message { margin-bottom: 15px; }
    .chatbot-message.user { text-align: right; }
    .chatbot-message.assistant { text-align: left; }
    .chatbot-message-content { display: inline-block; max-width: 80%; padding: 12px 16px; border-radius: 18px; }
    .chatbot-message.user .chatbot-message-content { background: #667eea; color: white; }
    .chatbot-message.assistant .chatbot-message-content { background: #f1f3f4; color: #333; }
    
    .chatbot-input { padding: 20px; border-top: 1px solid #e1e5e9; }
    .chatbot-input-group { display: flex; gap: 10px; }
    .chatbot-input-group input { flex: 1; padding: 12px; border: 2px solid #e1e5e9; border-radius: 25px; font-size: 16px; }
    .chatbot-input-group input:focus { outline: none; border-color: #667eea; }
    .chatbot-input-group button { padding: 12px 20px; border-radius: 25px; }
    
    .error { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; margin: 20px 0; border: 1px solid #f5c6cb; }
    .notice { background: #d1ecf1; color: #0c5460; padding: 15px; border-radius: 8px; margin: 20px 0; border: 1px solid #bee5eb; }
    .success { background: #d4edda; color: #155724; padding: 15px; border-radius: 8px; margin: 20px 0; border: 1px solid #c3e6cb; }
    
    .loading { text-align: center; padding: 20px; color: #666; }
    .loading::after { content: ''; display: inline-block; width: 20px; height: 20px; border: 2px solid #f3f3f3; border-top: 2px solid #667eea; border-radius: 50%; animation: spin 1s linear infinite; margin-left: 10px; }
    
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    
    .ai-status { background: #e8f5e8; border: 1px solid #4caf50; border-radius: 8px; padding: 15px; margin-bottom: 20px; }
    .ai-status.error { background: #ffebee; border-color: #f44336; }
    .ai-status.warning { background: #fff3e0; border-color: #ff9800; }
    
    .floating-chat-btn { position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 50%; cursor: pointer; font-size: 24px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.3s; z-index: 1000; }
    .floating-chat-btn:hover { transform: scale(1.1); }
    .floating-chat-btn.active { background: #dc3545; }
    
    .chat-overlay { position: fixed; bottom: 100px; right: 30px; width: 400px; height: 500px; background: white; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); z-index: 1001; display: none; }
    .chat-overlay.active { display: flex; flex-direction: column; }
    
    @media (max-width: 768px) {
      .main-content { grid-template-columns: 1fr; }
      .chatbot { height: 400px; }
      .chat-overlay { width: calc(100vw - 60px); height: 400px; }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🤖 MBS Clarity AI Assistant</h1>
      <p>Find the right MBS codes using natural language or chat with our AI assistant</p>
    </div>
    
    <div id="ai-status" class="ai-status">
      <div class="loading">Checking AI services...</div>
    </div>
    
    <div class="main-content">
      <div class="search-section">
        <h2>🔍 Search MBS Codes</h2>
        
        <div class="search-tabs">
          <button class="search-tab active" data-tab="natural">Natural Language</button>
          <button class="search-tab" data-tab="codes">Code Numbers</button>
        </div>
        
        <div id="natural-search" class="search-content active">
          <div class="input-group">
            <label for="natural-query">Describe the procedure or consultation:</label>
            <textarea id="natural-query" placeholder="e.g., 'I performed a consultation for a patient with chest pain, took history, examined them, and ordered tests'"></textarea>
          </div>
          <button class="btn" onclick="performNaturalLanguageSearch()">🔍 Find Matching Codes</button>
        </div>
        
        <div id="codes-search" class="search-content">
          <div class="input-group">
            <label for="codes">Enter MBS item numbers (comma-separated):</label>
            <input type="text" id="codes" placeholder="e.g., 3,23,104" />
          </div>
          <button class="btn" onclick="performCodeSearch()">🔍 Lookup Codes</button>
        </div>
        
        <div id="error" class="error" style="display: none;"></div>
        <div id="notice" class="notice" style="display: none;"></div>
        
        <div id="results" class="results"></div>
        <div id="ai-suggestions" class="ai-suggestions"></div>
        <div id="follow-up-questions" class="follow-up-questions"></div>
      </div>
      
      <div class="chatbot">
        <div class="chatbot-header">
          <h3>💬 AI Assistant</h3>
          <p>Ask questions about MBS codes</p>
        </div>
        <div id="chatbot-messages" class="chatbot-messages"></div>
        <div class="chatbot-input">
          <div class="chatbot-input-group">
            <input type="text" id="chatbot-input" placeholder="Ask me about MBS codes..." />
            <button class="btn" onclick="sendChatMessage()">Send</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <button id="floating-chat-btn" class="floating-chat-btn" onclick="toggleFloatingChat()">💬</button>
  
  <div id="chat-overlay" class="chat-overlay">
    <div class="chatbot-header">
      <h3>💬 AI Assistant</h3>
      <button class="btn btn-danger" onclick="toggleFloatingChat()" style="position: absolute; right: 15px; top: 15px; padding: 5px 10px;">✕</button>
    </div>
    <div id="floating-chat-messages" class="chatbot-messages"></div>
    <div class="chatbot-input">
      <div class="chatbot-input-group">
        <input type="text" id="floating-chat-input" placeholder="Ask me about MBS codes..." />
        <button class="btn" onclick="sendFloatingChatMessage()">Send</button>
      </div>
    </div>
  </div>

  <script>
    // Global variables
    let currentSessionId = null;
    let aiEnabled = false;
    let currentCodes = [];
    let searchHistory = [];
    
    // Initialize the application
    document.addEventListener('DOMContentLoaded', function() {
      checkAIStatus();
      initializeTabs();
      initializeChatbot();
      
      // Add enter key support for inputs
      document.getElementById('natural-query').addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && e.ctrlKey) {
          performNaturalLanguageSearch();
        }
      });
      
      document.getElementById('codes').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          performCodeSearch();
        }
      });
      
      document.getElementById('chatbot-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          sendChatMessage();
        }
      });
      
      document.getElementById('floating-chat-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          sendFloatingChatMessage();
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
            <small>Natural language search and chatbot are available</small>
          `;
        } else {
          aiEnabled = false;
          statusDiv.className = 'ai-status warning';
          statusDiv.innerHTML = `
            <strong>⚠️ AI Services Limited</strong><br>
            <small>Basic code lookup available. AI features require OpenAI API key.</small>
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
    
    // Initialize search tabs
    function initializeTabs() {
      const tabs = document.querySelectorAll('.search-tab');
      const contents = document.querySelectorAll('.search-content');
      
      tabs.forEach(tab => {
        tab.addEventListener('click', function() {
          const targetTab = this.getAttribute('data-tab');
          
          // Update tab states
          tabs.forEach(t => t.classList.remove('active'));
          this.classList.add('active');
          
          // Update content states
          contents.forEach(c => c.classList.remove('active'));
          document.getElementById(targetTab + '-search').classList.add('active');
        });
      });
    }
    
    // Initialize chatbot
    async function initializeChatbot() {
      if (!aiEnabled) return;
      
      try {
        const response = await fetch('/api/ai/chat/start', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({})
        });
        
        const data = await response.json();
        currentSessionId = data.session_id;
        
        addChatMessage('assistant', data.message);
      } catch (error) {
        console.error('Failed to initialize chatbot:', error);
      }
    }
    
    // Perform natural language search
    async function performNaturalLanguageSearch() {
      const query = document.getElementById('natural-query').value.trim();
      if (!query) {
        showError('Please describe the procedure or consultation.');
        return;
      }
      
      if (!aiEnabled) {
        showError('AI services are not available. Please use code number search instead.');
        return;
      }
      
      showLoading('Searching for matching MBS codes...');
      
      try {
        const response = await fetch('/api/ai/natural-language', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: query,
            context: {
              current_codes: currentCodes,
              search_history: searchHistory,
              session_id: currentSessionId
            }
          })
        });
        
        const data = await response.json();
        
        if (data.suggested_codes && data.suggested_codes.length > 0) {
          displayAISuggestions(data.detailed_suggestions);
          displayFollowUpQuestions(data.follow_up_questions);
          
          // Update context
          currentCodes = data.suggested_codes;
          searchHistory.push(query);
          
          showSuccess(`Found ${data.suggested_codes.length} matching MBS codes`);
        } else {
          showNotice('No matching codes found. Try providing more specific details about the procedure.');
        }
        
      } catch (error) {
        showError('Search failed: ' + error.message);
      }
    }
    
    // Perform code number search
    async function performCodeSearch() {
      const codesInput = document.getElementById('codes').value.trim();
      if (!codesInput) {
        showError('Please enter one or more MBS item numbers.');
        return;
      }
      
      const codes = codesInput.split(',').map(c => c.trim()).filter(c => c);
      if (codes.length === 0) {
        showError('Please enter valid MBS item numbers.');
        return;
      }
      
      showLoading('Looking up MBS codes...');
      
      try {
        const response = await fetch('/api/items?codes=' + encodeURIComponent(codes.join(',')));
        const data = await response.json();
        
        if (data.items && data.items.length > 0) {
          displayResults(data.items);
          currentCodes = codes;
          showSuccess(`Found ${data.items.length} MBS codes`);
        } else {
          showNotice('No codes found. Please check the item numbers.');
        }
        
      } catch (error) {
        showError('Lookup failed: ' + error.message);
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
          <div class="suggestion">
            <div class="suggestion-header">
              <span class="suggestion-code">Code ${suggestion.item_num}</span>
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
    
    // Display search results
    function displayResults(items) {
      const container = document.getElementById('results');
      
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
          addRelatedCode(targetCode);
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
    
    // Add related code
    function addRelatedCode(code) {
      const inputField = document.getElementById('codes');
      if (inputField) {
        const currentCodes = inputField.value ? inputField.value.split(',').map(c => c.trim()) : [];
        if (!currentCodes.includes(code)) {
          currentCodes.push(code);
          inputField.value = currentCodes.join(', ');
          performCodeSearch();
        }
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
    
    // Chatbot functions
    async function sendChatMessage() {
      const input = document.getElementById('chatbot-input');
      const message = input.value.trim();
      
      if (!message) return;
      
      addChatMessage('user', message);
      input.value = '';
      
      if (!aiEnabled) {
        addChatMessage('assistant', 'AI services are not available. Please use the code lookup feature instead.');
        return;
      }
      
      try {
        const response = await fetch('/api/ai/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            session_id: currentSessionId,
            message: message,
            context: {
              current_codes: currentCodes,
              search_history: searchHistory
            }
          })
        });
        
        const data = await response.json();
        addChatMessage('assistant', data.message);
        
        // Handle code suggestions
        if (data.code_suggestions && data.code_suggestions.length > 0) {
          displayChatbotSuggestions(data.code_suggestions);
        }
        
        // Handle follow-up questions
        if (data.follow_up_questions && data.follow_up_questions.length > 0) {
          displayChatbotFollowUpQuestions(data.follow_up_questions);
        }
        
      } catch (error) {
        addChatMessage('assistant', 'Sorry, I encountered an error: ' + error.message);
      }
    }
    
    // Floating chat functions
    function toggleFloatingChat() {
      const overlay = document.getElementById('chat-overlay');
      const btn = document.getElementById('floating-chat-btn');
      
      if (overlay.classList.contains('active')) {
        overlay.classList.remove('active');
        btn.classList.remove('active');
      } else {
        overlay.classList.add('active');
        btn.classList.add('active');
        initializeFloatingChat();
      }
    }
    
    function initializeFloatingChat() {
      const messages = document.getElementById('floating-chat-messages');
      const mainMessages = document.getElementById('chatbot-messages');
      
      if (mainMessages) {
        messages.innerHTML = mainMessages.innerHTML;
      }
    }
    
    async function sendFloatingChatMessage() {
      const input = document.getElementById('floating-chat-input');
      const message = input.value.trim();
      
      if (!message) return;
      
      addFloatingChatMessage('user', message);
      input.value = '';
      
      // Also send to main chatbot
      document.getElementById('chatbot-input').value = message;
      await sendChatMessage();
      
      // Update floating chat with response
      setTimeout(() => {
        const mainMessages = document.getElementById('chatbot-messages');
        const floatingMessages = document.getElementById('floating-chat-messages');
        if (mainMessages && floatingMessages) {
          floatingMessages.innerHTML = mainMessages.innerHTML;
        }
      }, 1000);
    }
    
    // Add chat message
    function addChatMessage(role, content) {
      const container = document.getElementById('chatbot-messages');
      const messageDiv = document.createElement('div');
      messageDiv.className = `chatbot-message ${role}`;
      
      const contentDiv = document.createElement('div');
      contentDiv.className = 'chatbot-message-content';
      contentDiv.textContent = content;
      
      messageDiv.appendChild(contentDiv);
      container.appendChild(messageDiv);
      container.scrollTop = container.scrollHeight;
    }
    
    // Add floating chat message
    function addFloatingChatMessage(role, content) {
      const container = document.getElementById('floating-chat-messages');
      const messageDiv = document.createElement('div');
      messageDiv.className = `chatbot-message ${role}`;
      
      const contentDiv = document.createElement('div');
      contentDiv.className = 'chatbot-message-content';
      contentDiv.textContent = content;
      
      messageDiv.appendChild(contentDiv);
      container.appendChild(messageDiv);
      container.scrollTop = container.scrollHeight;
    }
    
    // Display chatbot suggestions
    function displayChatbotSuggestions(suggestions) {
      suggestions.forEach(suggestion => {
        addChatMessage('assistant', `💡 Suggested Code ${suggestion.item_num}: ${suggestion.reasoning}`);
      });
    }
    
    // Display chatbot follow-up questions
    function displayChatbotFollowUpQuestions(questions) {
      questions.forEach(question => {
        addChatMessage('assistant', `❓ ${question}`);
      });
    }
    
    // Utility functions
    function showError(message) {
      const errorDiv = document.getElementById('error');
      errorDiv.textContent = message;
      errorDiv.style.display = 'block';
      document.getElementById('notice').style.display = 'none';
    }
    
    function showNotice(message) {
      const noticeDiv = document.getElementById('notice');
      noticeDiv.textContent = message;
      noticeDiv.style.display = 'block';
      document.getElementById('error').style.display = 'none';
    }
    
    function showSuccess(message) {
      const noticeDiv = document.getElementById('notice');
      noticeDiv.textContent = message;
      noticeDiv.className = 'success';
      noticeDiv.style.display = 'block';
      document.getElementById('error').style.display = 'none';
    }
    
    function showLoading(message) {
      const noticeDiv = document.getElementById('notice');
      noticeDiv.innerHTML = `<div class="loading">${message}</div>`;
      noticeDiv.style.display = 'block';
      document.getElementById('error').style.display = 'none';
    }
  </script>
</body>
</html>
"""
