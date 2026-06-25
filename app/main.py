from generation import generate_answer

while True:
    query = input("Ask a question or type 'stop' to exit: ")

    if query.lower() == "stop":
        break

    answer = generate_answer(query)