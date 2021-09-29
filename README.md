## This is a code challenge for students at TwentyThree
- Author: Mário Gažo
- Date: 2021, September
<hr>

## How to use?
- Part 1:

CLI tool is written as Python script

Before script is used some dependencies have to be installed, run:
```
pip install -r requirements.txt
```

Script sage: <br>
```
py twentythree.py method [id] [--type <photo|video>] [--title <title>] [--label <label>] [--url <valid url>]
```

To execute tests, run given command in the root directory:
```
python -m pytest
```

- Part 2

Microservice is written using Node.js

Install dependencies using:
```
npm install
```

Run project using:
```
node server.js
```
