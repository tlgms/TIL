<!-- notion-page-id: 3a02cdd741ac80609d48f435220779e4 -->

# Model 객체

controller의 데이터를 view로 전달하는 객체

```java
@RequestMapping("/board/view")
public String view(Model model) {
	model.addAttribute("id","hongku");
	return "board/view";
}
```

```java
model.addAttribute("변수이름", "변수에 넣을 데이터값");
```

위대로 적으면 스프링은 그 값을 view로 넘겨준다.

view 파일(html)에 ${}를 이용해서 값을 가져온다.

```html
<body>
<h1>view.jsp 입니다. </h1>
당신의 ID는 ${id} 입니다.
            //여기서의 id가 model.addAttribute("id","hongku"); 에서의 id이다.
</body>
```

<modelAndView 객체>

```java
@RequestMapping("/board/view")
public modelAndView content() {
	modelAndView mv = new ModelAndView();
	mv.setViewName("/board/content"); //view 이름
	
}
```
