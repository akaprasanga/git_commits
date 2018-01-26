import requests
api_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

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

#managing jason response
new = reply['data']['repository']['object']['history']['edges']
count=0
for each in new:
  count = count +1
  print(count)
  print(each['node'])
  print('\n')
  
