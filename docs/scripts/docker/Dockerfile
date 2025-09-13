FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps:
# - python3-tk: Tk GUI bindings for Matplotlib TkAgg
# - X11 libs: needed for windowing when forwarding to XQuartz
# - fonts-dejavu: avoids font warnings in Matplotlib
# NOTE: We do NOT install libatlas-base-dev (removed in trixie). SciPy wheels ship with OpenBLAS.
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    libx11-6 libxext6 libxrender1 libsm6 \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# Python deps
RUN pip install --no-cache-dir numpy scipy matplotlib

CMD ["/bin/bash"]
