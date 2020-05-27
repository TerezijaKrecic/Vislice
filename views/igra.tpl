% import model

% rebase('base.tpl')

  <h1>Vislice</h1>

  <blockquote>
    Let the fun begin!
  </blockquote>

  <h2> {{ igra.pravilni_del_gesla() }} </h2>

  Nepravilni ugibi: <b> {{ igra.nepravilni_del_gesla() }} </b> <br>
  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

  % if stanje == model.ZMAGA:
  <h3>Čestitam, uspelo ti je!</h3>
  <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % elif stanje == model.PORAZ:
  <h3>Žal vam ni uspelo.</h3>
  <p>Pravilno geslo je bilo <b>{{ igra.geslo }}</b></p>
  <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:
  <form action="/igra/" method="post">
    <!-- Črka: <input type='text' name='crka' maxlength='1'>
    <button type="submit">Ugibaj</button> -->
    <button type='submit' name='crka' value ='A'>A</button>
    <button type='submit' name='crka' value ='B'>B</button>
    <button type='submit' name='crka' value ='C'>C</button>
    <button type='submit' name='crka' value ='Č'>Č</button>
    <button type='submit' name='crka' value ='D'>D</button>
    <button type='submit' name='crka' value ='E'>E</button>
    <button type='submit' name='crka' value ='F'>F</button>
    <button type='submit' name='crka' value ='G'>G</button>
    <button type='submit' name='crka' value ='H'>H</button>
    <button type='submit' name='crka' value ='I'>I</button>
    <button type='submit' name='crka' value ='J'>J</button>
    <button type='submit' name='crka' value ='K'>K</button>
    <button type='submit' name='crka' value ='L'>L</button>
    <button type='submit' name='crka' value ='M'>M</button>
    <button type='submit' name='crka' value ='N'>N</button>
    <button type='submit' name='crka' value ='O'>O</button>
    <button type='submit' name='crka' value ='P'>P</button>
    <button type='submit' name='crka' value ='R'>R</button>
    <button type='submit' name='crka' value ='S'>S</button>
    <button type='submit' name='crka' value ='Š'>Š</button>
    <button type='submit' name='crka' value ='T'>T</button>
    <button type='submit' name='crka' value ='U'>U</button>
    <button type='submit' name='crka' value ='V'>V</button>
    <button type='submit' name='crka' value ='Z'>Z</button>
    <button type='submit' name='crka' value ='Ž'>Ž</button>


  </form>

  % end