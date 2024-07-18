from flask import Flask, request, render_template_string, send_file
import openai
import csv
import io
import logging

logging.basicConfig(level=logging.DEBUG)

openai.api_key = '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'


app = Flask(_name_)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test Case Generator Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            label, textarea, input { display: block; margin-bottom: 10px; }
            textarea { width: 100%; height: 100px; }
            button { padding: 10px 20px; }
        </style>
    </head>
    <body>
        <h1>Test Case Generator Chatbot</h1>
        <form id="testCaseForm" action="/generate_test_cases" method="POST" target="_blank">
            <label for="useCaseName">Use Case Name:</label>
            <input type="text" id="useCaseName" name="use_case_name" required>

            <label for="problemStatement">Problem Statement:</label>
            <textarea id="problemStatement" name="problem_statement" required></textarea>

            <button type="submit">Generate Test Cases</button>
        </form>
    </body>
    </html>
    ''')

@app.route('/generate_test_cases', methods=['POST'])
def generate_test_cases():
    use_case_name = request.form.get('use_case_name')
    problem_statement = request.form.get('problem_statement')

    if not use_case_name or not problem_statement:
        return "Use case name and problem statement are required."

    prompt = f"Generate detailed QA test cases for the following use case in an entertainment domain application:\n\nUse Case Name: {use_case_name}\nProblem Statement: {problem_statement}\n\nProvide test cases including solution, models to be used, and benefits."

    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=300
        )
        test_cases_text = response.choices[0].text.strip()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Use Case Name', 'Problem Statement', 'Solution'])
        for line in test_cases_text.split("\n"):
            writer.writerow([use_case_name, problem_statement, line])

        output.seek(0)
        return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', attachment_filename='test_cases.csv', as_attachment=True)

    except Exception as e:
        logging.error(f"Error during OpenAI API call: {e}")
        return "An error occurred while generating test cases."

if _name_ == '_main_':
    app.run(debug=True, threaded=True, port=5000)