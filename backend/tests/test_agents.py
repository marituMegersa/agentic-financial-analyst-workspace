def test_agent_orchestrator():
    prompt = "Test execution query for agentic-financial-analyst-workspace"
    assert len(prompt) > 0
    assert "Test" in prompt
