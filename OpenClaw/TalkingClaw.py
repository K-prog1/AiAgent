from openclaw import OpenClawClient

client = OpenClawClient(api_key="твой_ключ")

agent = client.agents.create(
    name="my_helper",
    model="anthropic/claude-sonnet-4-5",
    description="Помощник для задач",
    tools=["file_search", "web_search", "code_exec"]
)

workspace = client.workspaces.create(
    name="my_docs",
    intelligence_mode=True  
)
agent.mount_workspace(workspace.id)


client.files.upload(
    file_path="./notes/project.md",
    workspace_id=workspace.id
)


response = agent.run("Проанализируй проект и дай рекомендации")
print(response.output)


job = agent.run_async("Сгенерируй отчёт")

result = client.jobs.get(job.id)
print(result.output)