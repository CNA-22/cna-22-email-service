# Cloud Native Apps 22 Email Service

## GET /
- Just returns a message

## POST /sendmail
- Only valid school addresses allowed.

```
# POST application/json
{ 
    "to": "user@server.domain", 
    "subject": "Subject", 
    "body": "Body" 
}
```