import click
from .models import Task

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
@click.argument('description')
def add_task(title, description):
    task = Task(title=title, description=description)
    # Add code to save task to database
    print("Task added successfully!")

@cli.command()
def list_tasks():
    # Fetch tasks from database and display
    print("List of tasks:")
    # Add code to fetch tasks and print them

@cli.command()
@click.argument('task_id', type=int)
def complete_task(task_id):
    # Mark task as completed in database
    print(f"Task {task_id} marked as completed!")

if __name__ == '__main__':
    cli()
