---
# markdownlint-disable
# vale off
# tags used by just-the-docs theme
layout: default
parent: Contributing
nav_order: 7
has_children: false
has_toc: false
# vale  on
# markdownlint-enable
---

# my mermaid diagram

```mermaid
flowchart TD
    Start([Developer Request]) --> Load[Agent Loads Skill]
    Load --> |"SKILL.md + references<br/>(procedural guidance)"| Context[Skill in Context Window]
    
    Context --> Need{Need Current<br/>API Info?}
    
    Need -->|Yes| TryURL[Attempt Doc URL<br/>from training data]
    Need -->|No| Generate[Generate Code]
    
    TryURL --> URLWork{URL<br/>Resolves?}
    
    URLWork -->|Yes| Fetch[Fetch Documentation]
    URLWork -->|No - Moved| Search[Web Search]
    URLWork -->|No - 404| Search
    
    Search --> Found{Found<br/>Alternative?}
    Found -->|Yes| Fetch
    Found -->|No| Fallback[Use Training Data<br/>or Fabricate]
    
    Fetch --> Parse{Content<br/>Parseable?}
    
    Parse -->|Yes - Markdown| Extract[Extract Info]
    Parse -->|Yes - Clean HTML| Extract
    Parse -->|No - JS Rendered| Fallback
    Parse -->|Truncated >150k chars| Partial[Use Partial Content]
    
    Extract --> Combine[Combine Skill Guidance<br/>+ Doc Reference]
    Partial --> Combine
    Fallback --> Combine
    
    Combine --> Generate
    
    Generate --> Output([Code Output])
    
    style Start fill:#e1f5ff
    style Output fill:#e1f5ff
    style Fallback fill:#ffe1e1
    style Partial fill:#fff4e1
    style Extract fill:#e1ffe1
    ```

    whaddaya think!
