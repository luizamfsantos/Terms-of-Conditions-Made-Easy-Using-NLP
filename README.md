# TLTR (Too Long To Read)
TLTR is a python based project that reads "Terms and Conditions" inputed by the user and generate a score based on how invasive the terms are for the user. 

The application analyze the inputed data, find key words, and expose to the user any important information he should know.

This application is still under development and it was created during the HackWesTX Hackathon. 


##Prerequisites
- Python 3.6+
- Flask

```python
from flask import Flask, render_template, request, flash
  ```
  
- Rake 
```python
from multi_rake import Rake
```

## Built With

- Python (https://www.python.org/)
- Multi-Rake (https://pypi.org/project/multi-rake/)
- Flask (https://pypi.org/project/Flask/)
- Bootstrap (https://getbootstrap.com/)
- Love sz 

## Future Plans:
Our future goal is to:
1st) Use ML in a way the program will be able to read the Terms and Conditios and choose what words represent a benefit or a danger to the customer. 
     Because of the time constraint (and a team that was learning while doing it) we wouldnt have time to develop it during the hackathon. 
2nd) Develop a Google Chrome extension to facilitate even more the user experience. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors
Cris Caon 
Luiza Santos
Rafael Javarez
Pedro Piccino 

## License
[MIT](https://choosealicense.com/licenses/mit/)
multi-rake by vgrabovets as basis was used.
