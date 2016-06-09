#! tests for the rest APIs 

echo "requesting for phoneticd translation of word 'between hello word' :"
curl -H "Content-Type: application/json" -X GET -d '{"sentence":"between hello world"}' http://localhost:5000/translate
echo
echo "response received"

echo "requesting for phoneticd translation of word 'excited' :"
curl -H "Content-Type: application/json" -X GET -d '{"sentence":"excited"}' http://localhost:5000/translate
echo 
echo "response received"
