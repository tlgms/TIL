<!-- notion-page-id: 3c62cdd741ac8054882fcb7662025f85 -->

# 봉인된 인터페이스(Sealed Interface)

봉인된 인터페이스(Sealed Interface)는 해당 인터페이스를 구현(implements)하거나 확장(extends)할 수 있는 하위 클래스/인터페이스의 범위를 컴파일 타임에 제한하는 문법입니다.

---

```kotlin
sealed interface UiState

data object Loading : UiState
data class Success(val data: String) : UiState
data class Error(val exception: Throwable) : UiState

// when 식에서 모든 상태를 처리하므로 else 불필요
fun render(state: UiState) = when (state) {
    is Loading -> showProgressBar()
    is Success -> showContent(state.data)
    is Error -> showError(state.exception)
}
```
