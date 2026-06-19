from command_router import execute


def run_agent(prompt):

    prompt = prompt.lower()

    tasks = []

    separators = [

        " and then ",

        " then ",

        " and ",

        ","

    ]

    parts = [prompt]

    for sep in separators:

        new_parts = []

        for part in parts:

            new_parts.extend(part.split(sep))

        parts = new_parts

    for part in parts:

        part = part.strip()

        if part:

            tasks.append(part)

    results = []

    for task in tasks:

        try:

            result = execute(task)

            if result:

                results.append(result)

        except Exception as e:

            results.append(str(e))

    return "\n".join(results)