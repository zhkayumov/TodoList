import argparse
import loguru
import json



def open_storage():
    """
    Open our todo.json
    """
    with open("todo.json'", "r") as read_file:
        data = json.load(read_file)
        read_file.close()
    return data


def update_storage(new_data):
    """
    Update our todo.json
    """
    with open("todo.json'", "w") as read_file:
        json.dump(new_data, read_file)
        read_file.close()


def add_task(adding_task: str):
    """
    Add new task to todo.json
    """
    if adding_task is not None:
        new_task = {'title': adding_task[0], 'description': adding_task[1]}
        try:
            our_storage = open_storage()  # type: ignore
        except json.decoder.JSONDecodeError:
            our_storage = [new_task]
        else:
            our_storage.append(new_task)
        update_storage(our_storage)  # type: ignore
        loguru.logger.info('New task is added!')


def show_task(count_tasks: int):
    """
    Show last tasks
    """
    if count_tasks is not None:
        try:
            our_storage = open_storage()  # type: ignore
        except json.decoder.JSONDecodeError:
            print('Nothing to show')
        else:
            i = len(our_storage) - 1
            if count_tasks > len(our_storage):
                print('Try to show less count of tasks')
            else:
                count_tasks = i - count_tasks
            while count_tasks < i:
                print(our_storage[i])
                i -= 1


def do_task(done_task: str):
    """
    Delete task, that is done
    """
    if done_task is not None:
        try:
            our_storage = open_storage()  # type: ignore
        except json.decoder.JSONDecodeError:
            print('All is done, great job!')
        else:
            for task in our_storage:
                if task.get("title") == done_task:
                    i = our_storage.index(task)
                    our_storage.pop(i)
                    update_storage(our_storage)  # type: ignore
                    loguru.logger.info("Great job, " + done_task + ' is done!')


def find_task(finding_task: str):
    """
    Try to find task in todo.json
    """
    if finding_task is not None:
        try:
            our_storage = open_storage()  # type: ignore
        except json.decoder.JSONDecodeError:
            print('All is done, great job!')
        else:
            for task in our_storage:
                if finding_task in task.get("title") or finding_task in task.get("description"):
                    print(task)


def main():
    """
    The main function. It starts when the program is called.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-add', action="store", dest="adding_task", nargs=2, default=None, type=str)
    parser.add_argument('-show', action="store", dest="count_tasks", default=None, type=int)
    parser.add_argument('-done', action="store", dest="done_task", default=None, type=str)
    parser.add_argument('-find', action="store", dest="finding_task", default=None, type=str)

    args = parser.parse_args()

    add_task(args.adding_task)
    show_task(args.count_tasks)
    do_task(args.done_task)
    find_task(args.finding_task)


if __name__ == '__main__':
    main()  # type: ignore
