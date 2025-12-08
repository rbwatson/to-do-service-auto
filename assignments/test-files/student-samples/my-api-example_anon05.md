# Code examples

**Author:** Edward McHam

## cURL example

Get all the backgrounds for the CV summary.

### cURL command

```shell
curl http://localhost:3000/bkgds
```

### cURL response

```json
[     
  {
    "bkgd": "Multilingual Content",
    "id": 1
  },
  {
    "bkgd": "Structured Authoring",
    "id": 2
  },
  {
    "bkgd": "Technical Writing",
    "id": 3
  },
  {
    "bkgd": "UI/Web Design",
    "id": 4
  }
]```

## Postman example

Get all the CV tools.

### Request

**Method**: GET

```shell
{{base_url}}/tools
```

_`{{base_url}}`_ = `http://localhost:3000`

### Postman response

```json
[
    {
        "tool": "Adobe FrameMaker",
        "type": "tw",
        "id": 1
    },
    {
        "tool": "Confluence",
        "type": "tw",
        "id": 2
    },
    {
        "tool": "Jira",
        "type": "tw",
        "id": 3
    },
    {
        "tool": "Markdown",
        "type": "tw",
        "id": 4
    },
    {
        "tool": "Oxygen XML",
        "type": "tw",
        "id": 5
    },
    {
        "tool": "SharePoint",
        "type": "tw",
        "id": 6
    },
    {
        "tool": "Visio",
        "type": "tw",
        "id": 7
    },
    {
        "tool": "Adobe Creative Suite",
        "type": "wd",
        "id": 8
    },
    {
        "tool": "Balsamiq Wireframes",
        "type": "wd",
        "id": 9
    },
    {
        "tool": "CSS3",
        "type": "wd",
        "id": 10
    },
    {
        "tool": "Drupal",
        "type": "wd",
        "id": 11
    },
    {
        "tool": "GIMP",
        "type": "wd",
        "id": 12
    },
    {
        "tool": "HTML5",
        "type": "wd",
        "id": 13
    },
    {
        "tool": "JavaScript",
        "type": "wd",
        "id": 14
    },
    {
        "tool": "JSON",
        "type": "wd",
        "id": 15
    },
    {
        "tool": "LESS",
        "type": "wd",
        "id": 16
    },
    {
        "tool": "Photoshop",
        "type": "wd",
        "id": 17
    },
    {
        "tool": "Responsive Design",
        "type": "wd",
        "id": 18
    },
    {
        "tool": "SASS",
        "type": "wd",
        "id": 19
    },
    {
        "tool": "WordPress",
        "type": "wd",
        "id": 20
    },
    {
        "tool": "YAML",
        "type": "wd",
        "id": 21
    }
]
```
