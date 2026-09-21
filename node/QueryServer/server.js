const http = require('http');

const server = http.createServer((req, res) => {
    // 1. 작은따옴표 대신 백틱 사용
    const baseURL = `http://${req.headers.host}`;
    const parsedURL = new URL(req.url, baseURL);

    if (parsedURL.pathname === '/api/search') {
        // 2. searchParams 오타 수정 및 'keyword' 따옴표 추가
        const keyword = parsedURL.searchParams.get('keyword');

        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html; charset=utf-8');
        
        if (keyword) {
            // 3. 작은따옴표 대신 백틱 사용
            res.end(`<h1> 검색 결과 </h1> <p>입력하신 검색어는 <strong>${keyword}</strong> 입니다.</p>`);
        } else {
            res.end('<h1> 검색 결과 </h1> <p>주소창 끝에 <strong>?keyword=원하는 단어</strong>를 추가하세요.</p>');
        }

    } else {
        res.statusCode = 404; // 없는 주소이므로 404가 더 적합합니다.
        res.setHeader('Content-Type', 'text/plain; charset=utf-8');
        // 4. 빠져있던 res.end 추가
        res.end('잘못된 요청입니다.');
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    // 5. 작은따옴표 대신 백틱 사용
    console.log(`검색 서버 실행 중: http://localhost:${PORT}/api/search`);
});