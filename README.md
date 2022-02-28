# Cloud Native Apps 22 Email Service

## API Documentation (Swagger)
https://cna-email-fw-teaching.rahtiapp.fi/api-docs/

## GET /
- Just returns a message

## POST /sendmail
- Valid token required
- SSL (https) only

```
POST {{baseUrl}}/sendmail
Content-Type: application/json
Authorization: Bearer {{token}}

{ 
    "to": "user@maildomain.fi", 
    "from: "sender@maildomain.fi (OPTIONAL)",
    "subject": "Subject", 
    "body": "Body" 
}
```

### Attachments
- Attachments not supported. Host you file somewhere and include a link in the mail body.
