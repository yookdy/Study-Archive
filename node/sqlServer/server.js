const http = require('http');
const mysql = require('mysql2');

require('dotenv').config();
const db = mysql.createConnection({
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    user: process.env.DB_USER,
    password:process.env.DB_PASSWORD,
    database: process.env.DB_NAME
});

db.connect((err) =>{
    if(err){
        console.error('DB 연결 실패:', err.message);
    }else{
        console.log('DB 연결 성공');
    }
});

const server = http.createServer((req,res) =>{
    if(req.url === '/api/users'){
        const query ='SELECT *FROM users';
        db.query(query, (err, results) => {
            if(err){
                res.statusCode = 500;
                res.setHeader('Content-Type', 'application/json; charset=utf-8');
                res.end(JSON.stringify({error: '서버 오류'}));
            }else{
                res.statusCode = 200;
                res.setHeader('Content-Type', 'application/json; charset=utf-8');
                res.end(JSON.stringify(results));
            }
        })
    }else{
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain; charset=utf-8');
        res.end('잘못된 요청입니다.');
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`SQL 데이터 서버 실행 중: http://localhost:${PORT}/api/users`);
})