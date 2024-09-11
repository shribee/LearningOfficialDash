## learning material
https://dash.plotly.com/installation

## create environment
conda env export --no-builds --from-history | findstr -v "^prefix: " > environment.yml 

## run dash app
python app.py