# Generador de tutoriales para guitarra

Un programa hecho en Django con VueJS para generar tutoriales para canciones de guitarra, primero se crea un nuevo tutorial, para después ir a la sección de capturas, cargar el video y realizar capturas de imagen con descripción que se irán guardando, las capturas se pueden editar, ordenar y borrar. Una vez hecho este proceso se va a la sección de generar y se mostraran las imágenes con las descripciones ordenadas en una galería que permite mostrar las imágenes con las aclaraciones de cada una.

El proyecto ha sido actualizado a su version 1.1 y ahora puede buscar por título ademas de filtrar por dificultad y genéro. Tambien puede mostrar estadísticas que muestran cuantos tutoriales hay por dificultad y genéro.

Si ejecutan el proyecto por primera vez deben crear la base de datos SQLite con los siguientes comandos : 

```
manage.py makemigrations
manage.py migrate 
```

Para ejecutar el proyecto se debe usar el comando : 

```
manage.py runserver 9999
```

Unas imágenes :

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-d0MFXjbr5Qj2-Tmmv55Qp2Z9ei11_3J1zM_21EM0hwfBloau55ZaaBfYmFOrRZErLpzN163PNr40J2IrdlOz6eKlz07tBEiYpcjc4slA5sNA9VoQJz3PHTOhqqOtrzc_x2bMcZ6eSWq5Vp7ghH7JE3_1PRiRwa39LhSfEDDFwHxbwopoGsoi1ahupH8/s1897/uno.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgw4LxE6Hz8o4Vv-W5mS86LsZzPW5I7KAKil4pmc7H-IjVpKFW9xpv2zQG2qeY1PjuUrydZyi0OTVAxEVcravJZGKAA9XIMlYLmfAdFDbrT_STQQ2ijM2tMXUXYsT2RcBzyXDbvVezdNsKjKOzyF7UmT2Gi5acoCe8qq_aiKxvTzx_jM07fBgUgyCesoNQ/s1895/dos.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3HPqMghtX-wHKiW081KGJQ-Ajnd-qAByb3MRPvNpXNOUJ2FqA6K7Z0KkIypqGvSM5aVBO4X8icShNPq-hQzllvrQq82pCDw7ePBLQYFf22JhizvJr2HRwUWS59AC_6tzvryx_B-LEJsY9PSPrfW5fXgwwaYR0DSUBg6hFNFg3pd7M2DR_6TA6ptup1O0/s1913/tres.png)

![screenshot]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAit8YtHSytId_okHC8f4JaZEsDyAp5NeQRtD3A9ikn-taigsooRD94EV-Wc6nuVoZ-RcbQH5BajdEWqu7tz8mg89isjQuJddyQMVt2QZBUnWFmzFCZJAwwX0NR8hWbLWOYio6O7qKy1W0WbV3xbx9IiOijDjATTi37qaGDsC3ZoZKsyIxnphlOkDw/s1919/4.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicdmweD0rceL5TQt5sl3moXILDckAQNjcle1wELaayzqce7E5xDmny__cYYniyYXFCUSJOStPgfp2oHTDe8FE4EsQAOc1j1NiECYvXvv_K7eYsbKf7hITpNVK9Zn08Qz4fQ7PmAWihlBMVoRg6pQOexPM64nJRcmmf5GTm90oxUjjPUs8A0MwT559hJmA/s1915/cuatro.png))

![screenshot]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4dwpsefLguy8SlQBF8f7dU4WSr_hV38Z9gUZ0uw5VEn1ftx7iTNHqMYg-idjzs7Bdlr9dW69abSX2Z_aw_pslnyZ9NcmMfMg4S1LYMlDXx4nDeJvJC_5lZOKAATTjZ36DMa-511k0Jf8lSzmW4FGBVotPW_sWF3QEBv0dnjO2qLEpcU5p7vYRTlQu/s1908/5.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXEy6xrswKVQe66-3pnUa6p8J53AIaudLYpCuzPZXO42zymS9c6RHiabfXOTyDbrFuOW3NNpuRssMzy1XX3_y5KsAARfa1Ggw4A5JnVZYVWOyJMHI6Vl_qAN9dR2FWo4Pa0IayaMTnd7Qek-ZWrK-e5h0nIJt_tYfXcaRBqgn4M8Gy5t5ZGovhnxRzuEg/s1906/cinco.png))
