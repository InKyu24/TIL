## Python

##### 조건문 (if문)

```python
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finish')
```

 

##### 비교 연산자

+ 부울 표현식은 T/F 질문을 통해 프로그램의 흐름을 결정한다.



##### Indentation

+ if문과 for문에서 `:` 뒤에 Indentation을 한다.
+ Indentation를 유지해서 블록의 범위를 표시한다.
+ if문과 for문에 맞춰 내어쓰기를 해서 블록의 끝을 표시한다.
+ 빈 줄이나 주석은 Indentation에 상관없이 무시된다.



##### 주의사항 - 탭을 끄자!

+ 띄어쓰기 네 번을 해서 Indentation을 한다.
+ 대부분의 텍스트 에디터는 ".py" 파일의 탭을 스페이스로 변환한다.
+ Python은 Indentation을 중요시하기 때문에 `Tap`과 `Space`를 혼동하면 "Indentation 에러"가 발생한다.



##### 다중 분기 조건문 구조

+ elif는 python의 또 다른 예약어이다.

  ```python
  if x < 2 :
      print('small')
  elif x < 10 :
      print('midium')
  else :
      print('large')
  print('ALL DONE')
  ```



##### try / except 구조

+ 위험한 코드는 try/except를 사용해 처리한다.

+ try 블록에 있는 코드가 성공하면 except 블록은 건너뛰게 되고, try 블록에 있는 코드가 실패하는 경우에는 except 블록을 실행한다.

  ```python
  yourNumber = input('Enter a number: ')
  try:
  	ival = int(yourNumber)
  except:
      ival = -1
  if ival > 0:
  	print('Nice work')
  else:
      print('Not a number')
  ```

  