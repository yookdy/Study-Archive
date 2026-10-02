const http = require('http');
const db = require('./database');

const server = http.createServer((req, res) =>{
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    if(req.url === '/api/users'){
        const query = 'SELECT * FROM users';
        db.query(query, (err,results) =>{
            if(err){
                res.statusCode = 500;
                res.end(JSON.stringify({error: err.message}));
            }
            else{
                res.end(JSON.stringify(results));
            }
        })
    }
    else if(req.url === 'api/ios-developers'){
        const query = 'SELECT * FROM users WHERE role = "iOS 개발자"';
        db.query(query, (err,results) =>{
            if(err){
                res.statusCode = 500;
                res.end(JSON.stringify({error: err.message}));
            }
            else{
                res.end(JSON.stringify(results));
            }
        })
    }
})

const PORT = 3000;
server.listen(PORT, () =>{
    console.log(`SQL 데이터 서버 실행 중: http://localhost:${PORT}/api/users`);
    console.log(`SQL 데이터 서버 실행 중: http://localhost:${PORT}/api/ios-developers`);
    console.log(`🔍 현재 연결된 DB 주소: ${process.env.DB_HOST}`);
})