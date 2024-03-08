## You can click other road tag to router other video in this website 

## Quick Start  ( Recommand run code under virtual env )

```bash
git clone https://github.com/as183789043/Django-Simple_Blog.git
cd Django-Simple_Blog
pip install -r requirements.txt
cd mblog
python .\manage.py runserver
```


## Some Image about Real-Time Video
![image](https://github.com/as183789043/Django-real-time-road-images/assets/56618553/073046b6-1acb-4d23-9f75-1f5d03846c6e)

![image](https://github.com/as183789043/Django-real-time-road-images/assets/56618553/81b88f45-fd6f-460f-bbd5-ff71000bd3cc)



## A Samll component which refresh current time interval 1000ms 

```javascript
    <script>
        setInterval(function () {
            $('#time').text(new Date().toLocaleString());
        }, 1000);
    </script>
```
