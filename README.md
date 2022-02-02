# Cloud Native Apps 22 Email Service

## GET /
- Just returns a message

## POST /sendmail
- Valid token required

```
POST {{baseUrl}}/sendmail
Content-Type: application/json
Authorization: Bearer {{token}}

{ 
    "to": "user@maildomain.fi", 
    "subject": "Subject", 
    "body": "Body" 
}
```