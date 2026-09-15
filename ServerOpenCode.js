

const http = require('http');

const server = http.createServer((req, res)=>{
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain; charset=utf-8');
  res.end('안녕하세요! 이곳은 나의 첫 Node.js 웹 서버입니다.');
});

const PORT = 3000;
server.listen(PORT, () =>{
  console.log('서버가 실행 중입니다! http://localhost:${PORT} 으로 접속해 보세요.');
});