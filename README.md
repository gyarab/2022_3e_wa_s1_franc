# Editor

- ctrl + d = množení kurzoru na vyznačené
- shift + alt = množení kurzoru v ose y
- ctrl + h = nahradit

# CSS

## Import

```html
<link href="link" rel="stylesheet" />
```

## import font

```css
@font-face {
    font-family: newFont;
    src: url(link);
}
```

## Podmínka velikosti obrazovky

```css
@media screen and (max-width: 1000px) {
  ...
}

```

## Initial letter

```css
p:first-of-type::first-letter {
        float: left;
        font-family: Georgia;
        font-size: max(calc(2vw * 2), 56px);
        line-height: max(2.9vw, 40px);
        padding-top: 12px;
        padding-right: 8px;
        padding-left: 7px;
    }
```

## Underline

```css
.podtrhnuto {
    display: inline-block;
    line-height: 1px;
    border-bottom: solid 0.4em orangered;
}
```

# SASS

## SASS x SCSS

SASS má stejné funkce jako SCSS, rozdíl je v syntaxii. SCSS má syntaxii shodnou s css doplněnou o další funkcionalitu. SASS syntaxe neobsahuje na konci příkazů středníky a nepoužívá složené závorky, ty nahrazuje odsazení kódu. Středníky nahrazuje konec řádky.
Je zapotřebí vybrat správnou příponu před zahájením kompilace.

## Proměnné

Hodnoty proměnných nastavených uvnitř složených závorek nezmění hodnotu dané proměnné globálně. Pro provedení globální změny je potřeva přidat !global na konec příkazu.

```scss
$myColor: red;
h1 {
  $myColor: green !global;
  color: $myColor; // je zelená
}

p {
  color: $myColor; // je také zelená díky !global
}
```

## Import dalších SCSS souborů

Vhodné např. pro vytvoření specifického souboru obsahujícího pouze proměnné.

```scss
@import "file name";
```

## Nesting

```scss
nav ul {
  color: red;
}
```

je stejné jako:

```scss
nav {
  ul {
  color: red;
  }
}
```

## Stavy

```scss
a {
    color: black;
    &:hover {
      color: white;
    }
  }
```

Je stejné jako:

```scss
a {
    color: black;
}
a:hover {
      color: white;
}
```

## Mixin

```scss
@mixin bordered($color, $width: 2px) { // Pokud takto uvedeme defaultní hodnotu, není poté parametr povinné uvést
  border: $width solid $color;
}

.mxDIv {
  @include bordered(blue, 1px);
}
```

## Extend

```scss
.button-basic  {
  border: none;
  padding: 15px 30px;
}
.button-report  {
  @extend .button-basic;
  background-color: red;
}
```

## Map

Funguje velmi podobně jako HashMapa.

```scss
$primary-color: #EE6352;
$secondary-color: #D16E8D;
$lighten: 5;
$darken: 25;

$colors: (
  primary: (
    base: $primary-color,
    light: lighten($primary-color, $lighten),
    dark: darken($primary-color, $darken),
  ),
  secondary: (
    base: $secondary-color,
    light: lighten($secondary-color, $lighten),
    dark: darken($secondary-color, $darken),
  )
```

### Funkce

```scss
@function clr($base, $shade: base) {
  $color: map-get(map-get($colors, $base), $shade);
  @return $color;
}
```

## Cykly

```scss
@each $key, $val in $colors {
  .text-#{$key} {
    color: clr($val);
  }
}

@for $i from 1 through 9 {
  .border-#{$i} {
    border: 10px * $i;
  }
}
```

## Logika

```scss
$a: true;
@if(true){

}@else{
  
}
```

# Bootstrap

## Positions

vertical: -y-

horizontal: -x-

left: -s-

right: -e-

top: -t-

bottom: -b-

## Breakpoints

|Breakpoint       |Class infix    |Dimensions |
|-----------------|---------------|-----------|
|Extra small      |None           |<576px     |
|Small            |sm             |≥576px     |
|Medium           |md             |≥768px     |
|Large            |lg             |≥992px     |
|Extra large      |xl             |≥1200px    |
|Extra extra large|xxl            |≥1400px    |

## SASS breakpoints

```sass
$sm  = 576px;
$md  = 768px;
$lg  = 992px;
$xl  = 1200px;
$xxl = 1400px;
```

## Containers

| |Extra small <576px|Small ≥576px|Medium ≥768px|Large ≥992px|X-Large ≥1200px|XX-Large ≥1400px|
|-------------|-------|-------------|-------|-------|---------|---------|
|.container       |100%     |540px  |720px  |960px  |1140px   |1320px   |
.container-sm     |100%     |540px  |720px  |960px  |1140px   |1320px   |
.container-md     |100%     |100%   |720px  |960px  |1140px   |1320px   |
.container-lg     |100%     |100%   |100%   |960px  |1140px   |1320px   |
.container-xl     |100%     |100%   |100%   |100%   |1140px   |1320px   |
.container-xxl    |100%     |100%   |100%   |100%   |100%     |1320px   |
.container-fluid  |100%     |100%   |100%   |100%   |100%     |100%     |

## Grid system

100% šířka -> 12 dílků

![alt col description](https://miro.medium.com/max/1400/1*Wg3dRY_fGQUvwhBplltkoQ.png)

```html
<div class="container text-center">
  <div class="row">
    <div class="col-4">
      Column
    </div>
    <div class="col-4">
      Column
    </div>
    <div class="col-4">
      Column
    </div>
  </div>
</div>
```

## Gutters

Padding between columns.
>.g-*

## Základní nav bar

 navbar-expand-lg -> udává, kdy dojde ke změně do zobrazení v podobě sandwitche

```html

<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

## karta

![alt karta](https://www.tutorialrepublic.com/lib/images/bootstrap-5/bootstrap-card.png)

```html

<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```
