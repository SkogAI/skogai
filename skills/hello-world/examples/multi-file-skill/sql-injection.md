# sql injection patterns

patterns for detecting potential SQL injection vulnerabilities.

## dangerous patterns

### string concatenation in queries

```javascript
// dangerous
const query = "SELECT * FROM users WHERE id = " + userId;
const query = `SELECT * FROM users WHERE name = '${userName}'`;

// safe
const query = "SELECT * FROM users WHERE id = ?";
db.query(query, [userId]);
```

### grep patterns

```
# javascript/typescript
SELECT.*\+.*         # string concatenation in SELECT
INSERT.*\+.*         # string concatenation in INSERT
UPDATE.*\+.*         # string concatenation in UPDATE
DELETE.*\+.*         # string concatenation in DELETE
SELECT.*\$\{.*\}     # template literals in SELECT
query\(.*\+.*\)      # concatenation in query calls

# python
"SELECT.*%.*%        # string formatting in SQL
f"SELECT.*\{.*\}     # f-strings in SQL
\.execute\(.*\+.*\)  # concatenation in execute
\.format\(           # .format() in SQL strings

# php
"SELECT.*\..*\.      # concatenation with .
mysql_query\(\$      # direct variable in mysql_query
```

## safe patterns to recommend

### parameterized queries (javascript)

```javascript
// mysql2
db.query('SELECT * FROM users WHERE id = ?', [userId]);

// postgres
client.query('SELECT * FROM users WHERE id = $1', [userId]);

// sqlite3
db.get('SELECT * FROM users WHERE id = ?', [userId]);
```

### orm usage (typescript)

```typescript
// typeorm
await userRepository.findOne({ where: { id: userId } });

// prisma
await prisma.user.findUnique({ where: { id: userId } });

// sequelize
await User.findByPk(userId);
```

## severity: critical

SQL injection is always critical when user input is involved.

## references

- https://owasp.org/www-community/attacks/SQL_Injection
- https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
