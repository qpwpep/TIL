# 📘 Git 핵심 요약

## 1. Git 기본 개념
- **Git**: 분산 버전 관리 시스템(DVCS), 로컬에서도 버전 관리 가능
- **GitHub**: Git 기반 원격 저장소 서비스

---

## 2. 기본 명령어 흐름
```bash
git clone <repo-url>        # 원격 저장소 복제
git status                  # 현재 상태 확인
git add <파일>              # 스테이징
git commit -m "메시지"      # 커밋
git push origin main        # 원격 저장소 반영
git pull                    # 원격 저장소에서 변경 사항 가져오기
```

---

## 3. 커밋 메시지 규칙 (Conventional Commits)
```text
<type>: <short summary>

feat     : 기능 추가
fix      : 버그 수정
docs     : 문서 작성
style    : 코드 포맷팅
refactor : 코드 구조 개선
test     : 테스트 관련
chore    : 기타 작업
```

예:
```text
feat: add login component
fix!: resolve crash on startup
BREAKING CHANGE: remove support for legacy API
```

---

## 4. pre-commit
- **코드 커밋 전에 자동 검사 수행**
```bash
pip install pre-commit
touch .pre-commit-config.yaml
pre-commit install
pre-commit run --all-files
```

---

## 5. 브랜치 전략과 명령어
```bash
git branch                # 로컬 브랜치 목록
git branch <name>        # 브랜치 생성
git switch <name>        # 브랜치 이동
git merge <branch>       # 브랜치 병합
git branch -D <name>     # 브랜치 삭제
git diff main <branch>   # 변경 비교
```

### 병합 충돌 해결
1. 충돌 파일에서 표시된 구역(`<<<<`, `====`, `>>>>`) 수정
2. `git add`, `git commit`