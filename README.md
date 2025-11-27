# is-in-iran

A lightweight Python library that checks whether a given geographic poin (latitude, longitude) lies inside the borders of **Iran**.

It loads an official MultiPolygon GeoJSON of Iran and performs a  
point-in-polygon check using **Shapely**.

یک کتابخانه پایتون سبک است که بررسی می‌کند آیا یک نقطه جغرافیایی (عرض جغرافیایی، طول جغرافیایی) در داخل مرزهای **ایران** قرار دارد یا خیر.
<br>
این کتابخانه یک GeoJSON رسمی چندضلعی از ایران را بارگذاری کرده و
بررسی نقطه در چندضلعی را با استفاده از **Shapely** انجام می‌دهد.

---

## 🚀 Installation

```bash
pip install is-in-iran
```

## 🎯 Usage

```python
from is_in_iran import is_in_iran


print(is_in_iran(35.6892, 51.3890))  # → True  (Tehran)
print(is_in_iran(40.4168, -3.7038))  # → False (Madrid)
```

• Input format: (latitude, longitude)
<br>
• CRS: WGS84 (standard GPS coordinates)
<br>
• Points exactly on the border also return True.

## Development Setup

1. Create and activate a virtual environment.
2. Install the package in editable mode:

```python
pip install -e .
```

### Running Tests

```python
pytest
```

## Resources

- [GeoJSON Source](https://github.com/datasets/geo-countries)
