import requests
api_token = "390cdc9a8ebd21f56d6f2b5eda79cc261e5788b2"

url = 'https://api.github.com/graphql'
json = { "query" : """{ 
repository(owner:"bitcoin",name:"bitcoin"){
  object(expression:"master"){
    ... on Commit {
      
      history(first:100 since:"2017-01-18T18:00:00Z"){
        totalCount
        edges{
          node{
            committedDate
            committer {
              date
              name
            }
            messageHeadline           
          }
        }
        
        
      }
    }
  }
}
    
  

}
    
""" }

headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=json, headers=headers)
reply = r.json()
print(reply)
# new = reply['data']

# print(new)
# print('\n')
# for each in new['nodes']:
#   print(each['name'],each['description'])
#   print('\n')