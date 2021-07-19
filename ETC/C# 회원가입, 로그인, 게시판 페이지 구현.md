## 회원가입, 로그인, 게시판 페이지 구현

### 1. 회원가입

#### Model Class 생성 (User.cs, Note.cs)

```c#
using System.ComponentModel.DataAnnotations;

namespace AspnetNote.MVC.Models
{
    public class User
    {
        // C#에서 어노테이션은 대괄호를 이용

        /// <summary>
        /// 사용자 번호
        /// </summary>
        [Key] // PK 설정
        public int UserNo { get; set; }

        /// <summary>
        /// 사용자 이름
        /// </summary>
        [Required] // Not Null 설정
        public string UserName { get; set; }

        /// <summary>
        /// 사용자 아이디
        /// </summary>
        [Required] // Not Null 설정
        public string UserId { get; set; }

        /// <summary>
        /// 사용자 비밀번호
        /// </summary>
        [Required] // Not Null 설정
        public string UserPassword { get; set; }

    }
}
```

```C#
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AspnetNote.MVC.Models
{
    public class Note
    {
        /// <summary>
        /// 게시판 번호
        /// </summary>
        [Key]
        public int NoteNo { get; set; }

        /// <summary>
        /// 게시판 제목
        /// </summary>
        [Required]
        public string NoteTitle { get; set; }

        /// <summary>
        /// 게시판 내용
        /// </summary>
        [Required]
        public string NoteContents { get; set; }

        /// <summary>
        /// 작성자 번호
        /// </summary>
        [Required]
        public int UserNo { get; set; }

        [ForeignKey("UserNo")] // 외래키 설정
        public virtual User User { get; set; }
    }
}
```



#### DB Context 생성

```c#
using AspnetNote.MVC.Models;
using Microsoft.EntityFrameworkCore;

namespace AspnetNote.MVC.DataContext
{
    // DbContext를 상속 (콜론 > java에서 implements 역할)
    public class AspnetNoteDbContext : DbContext
    {
        public DbSet<User> Users { get; set; }

        public DbSet<Note> Notes { get; set; }

        // 오버라이드 메서드
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(@"Server=localhost;Database=AspnetNoteDb;User Id=sa;Password=1313;");
        }
    }
}
```

#### Package Manager Console에 add-migration FirstMigration 입력

#### Package Manager Console에 update-database 입력



#### AccountController 생성

``` c#
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class AccountController : Controller
    {
        /// <summary>
        /// 회원가입
        /// </summary>
        /// <returns>회원가입 페이지</returns>
        [HttpGet]
        public IActionResult Register()
        {
            return View();
        }
        /// <summary>
        /// 회원가입 전송
        /// </summary>
        /// <param name="model"></param>
        /// <returns>회원가입 정상 작동 시 Index 패이지, 가입 불가 시 회원가입 페이지 그대로</returns>
        [HttpPost]
        public IActionResult Register(User model)
        {
            if (ModelState.IsValid)
            {
                // Java에서는 try(SqlSession){} catch(){} 와 같이 사용
                using (var db = new AspnetNoteDbContext())
                {
                    db.Users.Add(model); // 메모리에 올리는 작업
                    db.SaveChanges(); // 실제 SQL로 저장하는 작업
                }
                return RedirectToAction("Index", "Home"); // 해당 action을 HomeController의 Index로 보냄
            }
            return View();
        }
    }
}

```



#### View 페이지 (Register.cshtml) 생성

```asp
@model AspnetNote.MVC.Models.User

<h2>회원가입</h2>

<form class="form" method="post" asp-controller="Account" asp-action="Register">
    <div class="form-group">
        <label>사용자 ID</label>
        <input type="text" class="form-control" asp-for="UserId" placeholder="사용자 ID 입력" />
        <span class="text-danger" asp-validation-for="UserId"></span>
    </div>
    <div class="form-group">
        <label>사용자 비밀번호</label>
        <input type="password" class="form-control" asp-for="UserPassword" placeholder="사용자 비밀번호 입력" />
        <span class="text-danger" asp-validation-for="UserPassword"></span>
    </div>
    <div class="form-group">
        <label>사용자 이름</label>
        <input type="text" class="form-control" asp-for="UserName" placeholder="사용자 이름 입력" />
        <span class="text-danger" asp-validation-for="UserName"></span>
    </div>
    <div class="form-group">
        <button type="submit" class="btn btn-primary">회원가입</button>
        <button class="btn btn-warning" href="#">취소</button>
    </div>
</form>
```



### 2. 로그인

#### AccountController에 Login 추가

```c#
using System;
using System.Linq;
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using AspnetNote.MVC.ViewModel;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class AccountController : Controller
    {
        /// <summary>
        /// 로그인
        /// </summary>
        /// <returns>로그인 페이지</returns>
        [HttpGet] // 해당 어노테이션이 없어도 자동으로 들어가는 방식 GET
        public IActionResult Login()
        {
            return View();
        }
        /// <summary>
        /// 로그인 전송
        /// </summary>
        /// <param name="model"></param>
        /// <returns></returns>
        [HttpPost]
        public IActionResult Login(LoginViewModel model)
        {
            if (ModelState.IsValid)
            {
                using (var db = new AspnetNoteDbContext())
                {
                    // Linq(Language-Intergrated Query): method chaining
                    var user = db.Users.FirstOrDefault(u => u.UserId.Equals(model.UserId) && u.UserPassword.Equals(model.UserPassword));
                    if (user != null)
                    {
                        // 로그인 성공 시
                        return RedirectToAction("LoginSuccess", "Home");
                    }
                }
            }
            // 로그인 실패 시
            ModelState.AddModelError(string.Empty, "사용자 ID 혹은 비밀번호가 올바르지 않습니다.");
            return View(model);
        }


        /// <summary>
        /// 회원가입
        /// </summary>
        /// <returns>회원가입 페이지</returns>
        [HttpGet]
        public IActionResult Register()
        {
            return View();
        }
        /// <summary>
        /// 회원가입 전송
        /// </summary>
        /// <param name="model"></param>
        /// <returns>회원가입 정상 작동 시 Index 패이지, 가입 불가 시 회원가입 페이지 그대로</returns>
        [HttpPost]
        public IActionResult Register(User model)
        {
            if (ModelState.IsValid)
            {
                // Java에서는 try(SqlSession){} catch(){} 와 같이 사용
                using (var db = new AspnetNoteDbContext())
                {
                    db.Users.Add(model); // 메모리에 올리는 작업
                    db.SaveChanges(); // 실제 SQL로 저장하는 작업
                }
                return RedirectToAction("Index", "Home"); // 해당 action을 HomeController의 Index로 보냄
            }
            return View();
        }
    }
}
```

#### HomeController에 LoginSuccess 추가 및 LoginSuccess.cshtml 추가



#### LoginViewModel 생성

Login에서는 UserName을 가져오지 않기 때문에, 회원가입까지 구현되어 있는 Model을 이용하게 되면 제대로 기능을 수행하지 못한다. 따라서 LoginViewModel을 생성한다.

```c#
using System.ComponentModel.DataAnnotations;

namespace AspnetNote.MVC.ViewModel
{
    public class LoginViewModel
    {
        [Required(ErrorMessage ="사용자 ID를 입력하세요.")]
        public string UserId { get; set; }

        [Required(ErrorMessage ="사용자 비밀번호를 입력하세요.")]
        public string UserPassword { get; set; }
    }
}
```



#### Login.cshtml 작성

```asp
@model AspnetNote.MVC.ViewModel.LoginViewModel
<h2>로그인</h2>

<form class="form" method="post" asp-controller="Account" asp-action="Login">
    <div class="text-danger" asp-validation-summary="ModelOnly"></div>
    <div class="form-group">
        <label>사용자 ID</label>
        <input type="text" asp-for="UserId" class="form-control" placeholder="사용자 ID 입력" />
        <span class="text-danger" asp-validation-for="UserId"></span>
    </div>

    <div class="form-group">
        <label>비밀번호</label>
        <input type="password" asp-for="UserPassword" class="form-control" placeholder="비밀번호 입력" />
        <span class="text-danger" asp-validation-for="UserPassword"></span>
    </div>

    <div class="form-group">
        <button type="submit" class="btn btn-success">로그인</button>
    </div>
</form>
```



#### Start.cs에 세션 사용 등록

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace AspnetNote.MVC
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllersWithViews();

            // DI 의존성 주입

            // Session - 서비스에 등록함
            services.AddSession();
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Home/Error");
            }
            app.UseStaticFiles();

            // 해당 application에서 사용
            app.UseSession();

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
            });
        }
    }
}
```



#### AccountController에서 로그인 성공 시 세션 넣기

```c#
using System;
using System.Linq;
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using AspnetNote.MVC.ViewModel;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class AccountController : Controller
    {
        /// <summary>
        /// 로그인
        /// </summary>
        /// <returns>로그인 페이지</returns>
        [HttpGet] // 해당 어노테이션이 없어도 자동으로 들어가는 방식 GET
        public IActionResult Login()
        {
            return View();
        }
        /// <summary>
        /// 로그인 전송
        /// </summary>
        /// <param name="model"></param>
        /// <returns></returns>
        [HttpPost]
        public IActionResult Login(LoginViewModel model)
        {
            if (ModelState.IsValid)
            {
                using (var db = new AspnetNoteDbContext())
                {
                    // Linq(Language-Intergrated Query): method chaining
                    var user = db.Users.FirstOrDefault(u => u.UserId.Equals(model.UserId) && u.UserPassword.Equals(model.UserPassword));
                    if (user != null)
                    {
                        // 로그인 성공 시
                        HttpContext.Session.SetInt32("USER_LOGIN_KEY", user.UserNo); // 세션 넣기
                        return RedirectToAction("LoginSuccess", "Home");
                    }
                }
            }
            // 로그인 실패 시
            ModelState.AddModelError(string.Empty, "사용자 ID 혹은 비밀번호가 올바르지 않습니다.");
            return View(model);
        }


        /// <summary>
        /// 회원가입
        /// </summary>
        /// <returns>회원가입 페이지</returns>
        [HttpGet]
        public IActionResult Register()
        {
            return View();
        }
        /// <summary>
        /// 회원가입 전송
        /// </summary>
        /// <param name="model"></param>
        /// <returns>회원가입 정상 작동 시 Index 패이지, 가입 불가 시 회원가입 페이지 그대로</returns>
        [HttpPost]
        public IActionResult Register(User model)
        {
            if (ModelState.IsValid)
            {
                // Java에서는 try(SqlSession){} catch(){} 와 같이 사용
                using (var db = new AspnetNoteDbContext())
                {
                    db.Users.Add(model); // 메모리에 올리는 작업
                    db.SaveChanges(); // 실제 SQL로 저장하는 작업
                }
                return RedirectToAction("Index", "Home"); // 해당 action을 HomeController의 Index로 보냄
            }
            return View();
        }
    }
}
```



### 로그아웃

#### AccountController.cs에 Logout 추가

```c#
using System;
using System.Linq;
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using AspnetNote.MVC.ViewModel;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class AccountController : Controller
    {
        /// <summary>
        /// 로그인
        /// </summary>
        /// <returns>로그인 페이지</returns>
        [HttpGet] // 해당 어노테이션이 없어도 자동으로 들어가는 방식 GET
        public IActionResult Login()
        {
            return View();
        }
        /// <summary>
        /// 로그인 전송
        /// </summary>
        /// <param name="model"></param>
        /// <returns></returns>
        [HttpPost]
        public IActionResult Login(LoginViewModel model)
        {
            if (ModelState.IsValid)
            {
                using (var db = new AspnetNoteDbContext())
                {
                    // Linq(Language-Intergrated Query): method chaining
                    var user = db.Users.FirstOrDefault(u => u.UserId.Equals(model.UserId) && u.UserPassword.Equals(model.UserPassword));
                    if (user != null)
                    {
                        // 로그인 성공 시
                        HttpContext.Session.SetInt32("USER_LOGIN_KEY", user.UserNo); // 세션 넣기
                        return RedirectToAction("LoginSuccess", "Home");
                    }
                }
            }
            // 로그인 실패 시
            ModelState.AddModelError(string.Empty, "사용자 ID 혹은 비밀번호가 올바르지 않습니다.");
            return View(model);
        }

        /// <summary>
        /// 로그아웃
        /// </summary>
        /// <returns>세션 지우고, 메인화면으로 이동</returns>
        public IActionResult Logout()
        {
            // HttpContext.Session.Clear();  존재하는 세션 모두 지우기
            HttpContext.Session.Remove("USER_LOGIN_KEY"); // 해당 세션 지우기
            return RedirectToAction("Index", "Home");
        }
        
        /// <summary>
        /// 회원가입
        /// </summary>
        /// <returns>회원가입 페이지</returns>
        [HttpGet]
        public IActionResult Register()
        {
            return View();
        }
        /// <summary>
        /// 회원가입 전송
        /// </summary>
        /// <param name="model"></param>
        /// <returns>회원가입 정상 작동 시 Index 패이지, 가입 불가 시 회원가입 페이지 그대로</returns>
        [HttpPost]
        public IActionResult Register(User model)
        {
            if (ModelState.IsValid)
            {
                // Java에서는 try(SqlSession){} catch(){} 와 같이 사용
                using (var db = new AspnetNoteDbContext())
                {
                    db.Users.Add(model); // 메모리에 올리는 작업
                    db.SaveChanges(); // 실제 SQL로 저장하는 작업
                }
                return RedirectToAction("Index", "Home"); // 해당 action을 HomeController의 Index로 보냄
            }
            return View();
        }
    }
}
```



#### 로그아웃  버튼 추가

```asp
@using Microsoft.AspNetCore.Http;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>@ViewData["Title"] - AspnetNote.MVC</title>
    <link rel="stylesheet" href="~/lib/bootstrap/dist/css/bootstrap.min.css" />
    <link rel="stylesheet" href="~/css/site.css" />
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-sm navbar-toggleable-sm navbar-light bg-white border-bottom box-shadow mb-3">
            <div class="container">
                <a class="navbar-brand" asp-area="" asp-controller="Home" asp-action="Index">AspnetNote.MVC</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".navbar-collapse" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="navbar-collapse collapse d-sm-inline-flex flex-sm-row-reverse">
                    <ul class="navbar-nav flex-grow-1">
                        <li class="nav-item">
                            <a class="nav-link text-dark" asp-area="" asp-controller="Home" asp-action="Index">Home</a>
                        </li>
                        @if (Context.Session.GetInt32("USER_LOGIN_KEY") == null)
                        {
                            <li class="nav-item ml-auto">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Account" asp-action="Register">Register</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Account" asp-action="Login">Login</a>
                            </li>
                        }
                        else
                        {
                            <li class="nav-item ml-auto">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Account" asp-action="Logout">Logout</a>
                            </li>
                        }
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    <div class="container">
        <main role="main" class="pb-3">
            @RenderBody()
        </main>
    </div>

    <footer class="border-top footer text-muted">
        <div class="container">
            &copy; 2021 - AspnetNote.MVC - <a asp-area="" asp-controller="Home" asp-action="Privacy">Privacy</a>
        </div>
    </footer>
    <script src="~/lib/jquery/dist/jquery.min.js"></script>
    <script src="~/lib/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
    <script src="~/js/site.js" asp-append-version="true"></script>
    @RenderSection("Scripts", required: false)
</body>
</html>
```



### 게시판 리스트 추가

#### NoteController 생성

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class NoteController : Controller
    {
        /// <summary>
        /// 게시판 리스트
        /// </summary>
        /// <returns></returns>
        public IActionResult Index()
        {
            using (var db = new AspnetNoteDbContext())
            {
                var list = db.Notes.ToList();
                return View(list);
            }
        }   
    }
}
```



### Note/Index.cshtml 작성

```asp
@model AspnetNote.MVC.Models.Note 
<table class="table table-bordered">
    <thead>
        <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
        </tr>
    </thead>
    <tbody>
        @foreach (var note in Model)
        {
            <tr>
                <td>@note.NoteNo</td>
                <td>@note.NoteTitle</td>
                <td>@note.UserNo</td>
            </tr>
        }
    </tbody>
</table>

<a class="btn btn-warning" asp-controller="Note" asp-action="Add">게시물 작성</a>
```



### 게시물 작성

#### NoteController에 Add 추가

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class NoteController : Controller
    {
        /// <summary>
        /// 게시판 리스트
        /// </summary>
        /// <returns></returns>
        public IActionResult Index()
        {
            using (var db = new AspnetNoteDbContext())
            {
                var list = db.Notes.ToList();
                return View(list);
            }
        }
        
        /// <summary>
        /// 게시글 추가
        /// </summary>
        /// <returns>게시물 작성 페이지 이동</returns>
        public IActionResult Add()
        {

            return View();
        }
        
        /// <summary>
        /// 게시글 추가
        /// </summary>
        /// <param name="model"></param>
        /// <returns>작성한 게시물 DB 저장</returns>
        [HttpPost]
        public IActionResult Add(Note model)
        {
            if (ModelState.IsValid)
            {
                using (var db = new AspnetNoteDbContext())
                {
                    db.Notes.Add(model);

                    if (db.SaveChanges() > 0)
                    {
                        return Redirect("index");
                    }
                }
                ModelState.AddModelError(string.Empty, "게시물을 저장할 수 없습니다.");
            }
            return View(model);
        }
    }
}
```



#### Add.cshtml 작성

```asp
@model AspnetNote.MVC.Models.Note
<div class="row">
    <div class="col-lg-4"></div>
    <div class="col-lg-4">
        <form class="form" method="post" asp-controller="Note" asp-action="Add">
            <div class="text-danger" asp-validation-summary="ModelOnly"></div>
            <div class="form-group">
                <label>제목</label>
                <input type="text" class="form-control" asp-for="NoteTitle" placeholder="글 제목 입력" />
                <span class="text-danger" asp-validation-for="NoteTitle"></span>
            </div>
            <div class="form-group">
                <textarea class="form-control" rows="15" asp-for="NoteContents" placeholder="글 내용 입력"></textarea>
                <span class="text-danger" asp-validation-for="NoteContents"></span>
            </div>

            <div class="form-group">
                <button type="submit" class="btn btn-primary">저장</button>
                <a class="btn" asp-controller="Note" asp-action="Index">취소</a>
            </div>
        </form>
    </div>
</div>
```



### * 로그인 세션 여부에 따라 게시판 접근 제한

#### NoteController 수정

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class NoteController : Controller
    {
        /// <summary>
        /// 게시판 리스트
        /// </summary>
        /// <returns></returns>
        public IActionResult Index()
        {
            if(HttpContext.Session.GetInt32("USER_LOGIN_KEY") == null)
            {
                // 로그인이 안된 상태
                return RedirectToAction("Login", "Account");
            }
            using (var db = new AspnetNoteDbContext())
            {
                var list = db.Notes.ToList();
                return View(list);
            }
        }

        /// <summary>
        /// 게시글 추가
        /// </summary>
        /// <returns>게시물 작성 페이지 이동</returns>
        public IActionResult Add()
        {
            if (HttpContext.Session.GetInt32("USER_LOGIN_KEY") == null)
            {
                // 로그인이 안된 상태
                return RedirectToAction("Login", "Account");
            }
            return View();
        }
        
        /// <summary>
        /// 게시글 추가
        /// </summary>
        /// <param name="model"></param>
        /// <returns>작성한 게시물 DB 저장</returns>
        [HttpPost]
        public IActionResult Add(Note model)
        {
            if (HttpContext.Session.GetInt32("USER_LOGIN_KEY") == null)
            {
                // 로그인이 안된 상태
                return RedirectToAction("Login", "Account");
            }
            if (ModelState.IsValid)
            {
                using (var db = new AspnetNoteDbContext())
                {
                    db.Notes.Add(model);

                    if (db.SaveChanges() > 0)
                    {
                        return Redirect("index");
                    }
                }
                ModelState.AddModelError(string.Empty, "게시물을 저장할 수 없습니다.");
            }
            return View(model);
        }
    }
}
```



### 게시글 상세보기

#### NoteController.cs에 Detail 추가

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AspnetNote.MVC.DataContext;
using AspnetNote.MVC.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AspnetNote.MVC.Controllers
{
    public class NoteController : Controller
    {
        /// <summary>
        /// 게시판 리스트
        /// </summary>
        /// <returns></returns>
        public IActionResult Index()
        {
            if(HttpContext.Session.GetInt32("USER_LOGIN_KEY") == null)
            {
                // 로그인이 안된 상태
                return RedirectToAction("Login", "Account");
            }
            using ( var db = new AspnetNoteDbContext())
            {
                List<Note> list = db.Notes.ToList();
                return View(list);
            }
        }

        /// <summary>
        /// 게시글 추가
        /// </summary>
        /// <returns>게시물 작성 페이지 이동</returns>
        public IActionResult Add()
        {
            if (HttpContext.Session.GetInt32("USER_LOGIN_KEY") == null)
            {
                // 로그인이 안된 상태
                return RedirectToAction("Login", "Account");
            }
            return View();
        }
        
        /// <summary>
        /// 게시글 추가
        /// </summary>
        /// <param name="model"></param>
        /// <returns>작성한 게시물 DB 저장</returns>
        [HttpPost]
        public IActionResult Add(Note model)
        {
            if (HttpContext.Session.GetInt32("USER_LOGIN_KEY") == null)
            {
                // 로그인이 안된 상태
                return RedirectToAction("Login", "Account");
            }

            model.UserNo = int.Parse(HttpContext.Session.GetInt32("USER_LOGIN_KEY").ToString());
            if (ModelState.IsValid)
            {
                using (var db = new AspnetNoteDbContext())
                {
                    db.Notes.Add(model);

                    if (db.SaveChanges() > 0)
                    {
                        return Redirect("index");
                    }
                }
                ModelState.AddModelError(string.Empty, "게시물을 저장할 수 없습니다.");
            }
            return View(model);
        }

        /// <summary>
        /// 게시글 상세보기
        /// </summary>
        /// <returns></returns>
        public IActionResult Detail(int noteNo)
        {
            if(HttpContext.Session.GetInt32("USER_LOGIN_KEY") == null)
            {
                // 로그인이 안된 상태
                return RedirectToAction("Login", "Account");
            }
            using (var db = new AspnetNoteDbContext())
            {
                var note = db.Notes.FirstOrDefault(n => n.NoteNo.Equals(noteNo));
                return View(note);
            }
        }
    }
}
```



#### Detail.cshtml 작성

```asp
<div class="row">
    <div class="col-lg-12">
        <h3 class="page-header">상세 읽기 - @Model.NoteTitle</h3>
    </div>
</div>

<div class="row">
    <div class="col-lg-10">
        <div class="card card-header">
            @Model.NoteTitle
        </div>
        <div class="card card-body">
            @Model.NoteContents
        </div>
        <div class="card-footer">
            <a class="btn btn-primary" asp-controller="Note" asp-action="Index">목록</a>
        </div>
    </div>
</div>
```



#### note/Index.cshtml 수정

```asp
<table class="table table-bordered">
    <thead>
        <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
        </tr>
    </thead>
    <tbody>
        @foreach (var note in Model)
        {
            <tr>
                <td>@note.NoteNo</td>
                <td>
                    <a asp-controller="Note" asp-action="Detail" asp-route-noteNo="@note.NoteNo">@note.NoteTitle</a>
                </td>
                <td>@note.UserNo</td>
            </tr>
        }
    </tbody>
</table>

<a class="btn btn-warning" asp-controller="Note" asp-action="Add">게시물 작성</a>
```



### * 자바스크립트 텍스트 에디터 적용

#### trumbowyg 추가

#### _Layout.cshtml 수정

```asp
@using Microsoft.AspNetCore.Http;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>@ViewData["Title"] - AspnetNote.MVC</title>
    <link rel="stylesheet" href="~/lib/bootstrap/dist/css/bootstrap.min.css" />
    <link rel="stylesheet" href="~/Trumbowyg/ui/trumbowyg.min.css">
    <link rel="stylesheet" href="~/css/site.css" />
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-sm navbar-toggleable-sm navbar-light bg-white border-bottom box-shadow mb-3">
            <div class="container">
                <a class="navbar-brand" asp-area="" asp-controller="Home" asp-action="Index">AspnetNote.MVC</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".navbar-collapse" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="navbar-collapse collapse d-sm-inline-flex flex-sm-row-reverse">
                    <ul class="navbar-nav flex-grow-1">
                        <li class="nav-item">
                            <a class="nav-link text-dark" asp-area="" asp-controller="Note" asp-action="Index">Note</a>
                        </li>
                        @if (Context.Session.GetInt32("USER_LOGIN_KEY") == null)
                        {
                            <li class="nav-item ml-auto">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Account" asp-action="Register">Register</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Account" asp-action="Login">Login</a>
                            </li>
                        }
                        else
                        {
                            <li class="nav-item ml-auto">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Account" asp-action="Logout">Logout</a>
                            </li>
                        }
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    <div class="container">
        <main role="main" class="pb-3">
            @RenderBody()
        </main>
    </div>

    <footer class="border-top footer text-muted">
        <div class="container">
            &copy; 2021 - AspnetNote.MVC - <a asp-area="" asp-controller="Home" asp-action="Privacy">Privacy</a>
        </div>
    </footer>
    <script src="~/lib/jquery/dist/jquery.min.js"></script>
    <script src="~/lib/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
    <script src="~/Trumbowyg/trumbowyg.min.js"></script>
    <script src="~/Trumbowyg/langs/ko.min.js"></script>
    <script src="~/js/site.js" asp-append-version="true"></script>
    @RenderSection("Scripts", required: false)
</body>
</html>
```



#### Add.cshtml 수정

```asp
@model AspnetNote.MVC.Models.Note

<div class="row">
    <div class="col-lg-8"></div>
    <div class="col-lg-8">
        <form class="form" method="post" asp-controller="Note" asp-action="Add">
            <div class="text-danger" asp-validation-summary="ModelOnly"></div>
            <div class="form-group">
                <label>제목</label>
                <input type="text" class="form-control" asp-for="NoteTitle" placeholder="글 제목 입력" />
                <span class="text-danger" asp-validation-for="NoteTitle"></span>
            </div>
            <div class="form-group">
                <textarea class="form-control edit" asp-for="NoteContents" placeholder="글 내용 입력"></textarea>
                <span class="text-danger" asp-validation-for="NoteContents"></span>
            </div>

            <div class="form-group">
                <button type="submit" class="btn btn-primary">저장</button>
                <a class="btn" asp-controller="Note" asp-action="Index">취소</a>
            </div>
        </form>
    </div>
</div>
```



#### site.js 수정

```javascript
$(".edit").trumbowyg();
```



### 게시글 상세보기 페이지 수정 (텍스트 에디터로 수정된 글보기)

#### Detail.cshtml 수정

```asp
<div class="row">
    <div class="col-lg-12">
        <h3 class="page-header">상세 읽기 - @Model.NoteTitle</h3>
    </div>
</div>

<div class="row">
    <div class="col-lg-10">
        <div class="card card-header">
            @Model.NoteTitle
        </div>
        <div class="card card-body">
            @Html.Raw(Model.NoteContents)
        </div>
        <div class="card-footer">
            <a class="btn btn-primary" asp-controller="Note" asp-action="Index">목록</a>
        </div>
    </div>
</div>
```



### 텍스트 에디터에 이미지 파일 업로드

#### wwwroot 하위에 upload 폴더 생성

#### UploadController 생성

```c#
```
