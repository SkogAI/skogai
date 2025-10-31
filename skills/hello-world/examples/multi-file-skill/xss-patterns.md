# cross-site scripting (xss) patterns

patterns for detecting potential XSS vulnerabilities.

## dangerous patterns

### react

```javascript
// dangerous
<div dangerouslySetInnerHTML={{__html: userContent}} />
<div>{userContent}</div>  // if userContent is HTML string

// safe
<div>{userContent}</div>  // react escapes by default for text
<div dangerouslySetInnerHTML={{__html: DOMPurify.sanitize(userContent)}} />
```

### vanilla javascript

```javascript
// dangerous
element.innerHTML = userInput;
element.outerHTML = userInput;
document.write(userInput);
eval(userInput);

// safe
element.textContent = userInput;
element.setAttribute('data-value', userInput);
```

## grep patterns

```
# react
dangerouslySetInnerHTML.*\{.*\}     # dangerouslySetInnerHTML usage
dangerouslySetInnerHTML(?!.*DOMPurify)  # without DOMPurify

# javascript
\.innerHTML\s*=                      # innerHTML assignment
\.outerHTML\s*=                      # outerHTML assignment
document\.write\(                    # document.write
\.insertAdjacentHTML\(              # insertAdjacentHTML

# eval and similar
eval\(                               # eval usage
setTimeout\(.*,                      # setTimeout with string
setInterval\(.*,                     # setInterval with string
new Function\(                       # Function constructor
```

## context-specific checks

### user-controlled attributes

```javascript
// dangerous - user controls href
<a href={userInput}>link</a>

// check for javascript: protocol
if (userInput.startsWith('javascript:')) { /* dangerous */ }
```

### grep for href/src with variables

```
href=\{[a-zA-Z]      # variable in href
src=\{[a-zA-Z]       # variable in src
```

## safe patterns to recommend

### sanitization libraries

```javascript
// DOMPurify
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(dirty);

// isomorphic-dompurify (for ssr)
import DOMPurify from 'isomorphic-dompurify';
```

### validation

```javascript
// whitelist allowed protocols
const allowedProtocols = ['http:', 'https:', 'mailto:'];
const url = new URL(userInput);
if (!allowedProtocols.includes(url.protocol)) {
  throw new Error('Invalid protocol');
}
```

## severity: high

XSS is high severity when user-generated content is involved.

## references

- https://owasp.org/www-community/attacks/xss/
- https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
