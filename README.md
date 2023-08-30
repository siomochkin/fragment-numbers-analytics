# Fragment numbers analytics #

The project was developed for pasring data from the website https://fragment.com to create statistics on the cost of Telegram numbers.

## Installation
To install and run script you need to clone the repository and navigate to the project directory in your terminal:

```
git clone https://github.com/siomochkin/fragment-numbers-analytics.git
cd <repository_name>
```

Then create and activate virtual environment in your working directory:

``` 
python3 -m venv venv
source venv/bin/activate
```

Insatall required libs:

```
pip install -r requirements.txt
```

## Start
Run main.py file to start writing data from the website to your csv file:

```
python3 main.py
```
