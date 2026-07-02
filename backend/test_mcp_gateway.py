from backend.mcp.mcp_gateway import MCPGateway

gateway = MCPGateway()

print("Available Tools")
print(gateway.discover_tools())

print("\nHealth Check")
print(gateway.health_check())

print("\nAuthentication")
print(gateway.authenticate_tool("leave_service"))

print("\nVersion")
print(gateway.get_tool_version("knowledge_base"))

print("\nExecute Tool")
print(gateway.execute_tool("leave_service"))
