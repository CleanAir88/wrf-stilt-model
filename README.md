# WRF-STILT Model

An automated backward trajectory dispersion platform based on the WRF and STILT model for identifying potential source area. It supports containerized deployment via Docker, scheduled tasks via Django + Celery, and provides APIs for retrieving simulation results.

- 📘 [Learn more about STILT](https://uataq.github.io/stilt/#/install)  
- 🌍 [Learn more about Air Tracker](https://globalcleanair.org/air-tracker/map/)

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourame/wrf-stilt-model.git
cd wrf-stilt-model
```
### 2. Build the Docker image
```
docker build -t wrf-stilt-model .
```
### 3. Run the container
```
 First, create a data directory on the server to store meteorological files and computation results：
 mkdir （pwd）/data

 docker run -d --name wrf-stilt-model -p 8000:8000 -p 5555:5555 \
  -v $(pwd)/data:/src/data \
  gfs-stilt-model 

```

## STILT Executable Registration

In order to run STILT with forecast meteorology, you must obtain the official HYSPLIT binary.

Apply for access here:

https://www.ready.noaa.gov/HYSPLIT_register.php(https://www.ready.noaa.gov/HYSPLIT_register.php)

After registering, download the executables, unzip them, and copy to:
```
build/bin/linux-gnu/
```
Or place them directly into the Docker image under ${STILT_WD}/exe/.
