# Contributing to AFTEC

First off, thanks for taking the time to contribute! 🎉🌾

AFTEC is an open‑source project and we welcome all kinds of contributions – code, documentation, bug reports, feature ideas, or hardware integration guides.

The following is a set of guidelines for contributing to AFTEC. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

---

## 📦 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [INSERT EMAIL].

---

## 🧭 How Can I Contribute?

### 🐛 Reporting Bugs

- Use the **GitHub Issues** tab.
- Check if the bug has already been reported.
- If not, open a new issue with a **clear title** and a **detailed description**.
- Include steps to reproduce, expected behavior, actual behavior, and screenshots if helpful.
- Tell us your OS and Python version.

### 💡 Suggesting Enhancements

- Open an issue with label `enhancement`.
- Describe the feature, why it’s useful, and how it should work.
- If it’s a big change, we can discuss the architecture first.

### 📝 Improving Documentation

- Typos, unclear explanations, missing docstrings – all are welcome.
- You can edit files in `docs/` or directly in the `README.md`.
- For large doc changes, please open an issue first.

### 🔌 Adding a new Ingester, Storage, or Detector

We love modularity! To add a new component:

1. Create a new file in the appropriate subfolder:  
   - `src/aftec/ingesters/` for new data sources (MQTT, LoRa, file, etc.)
   - `src/aftec/storage/` for new backends (PostgreSQL, InfluxDB)
   - `src/aftec/detectors/` for new anomaly detection or prediction models
2. Inherit from the corresponding base class (`BaseIngester`, `BaseStorage`, `BaseDetector`).
3. Implement all abstract methods.
4. Write unit tests in `tests/`.
5. Update `__init__.py` if needed.
6. Open a pull request.

### 🧪 Writing Tests

- We use `pytest`.
- All new functionality should include tests.
- Run `make test` before pushing.
- Aim for at least 80% coverage on new code.

---

## 🚀 Pull Request Process

1. **Fork** the repository and create your branch from `main`.
2. If you’ve added code that should be tested, add tests.
3. Ensure your code passes all existing tests (`make test`).
4. Update the `README.md` or documentation if your changes require it.
5. Use a clear and descriptive PR title (e.g., `feat: add MQTT ingester`).
6. In the PR description, explain what your change does and why.
7. Link any related issues.
8. Wait for a maintainer to review. Be open to feedback.

> **Commit convention (optional but nice):**  
> Use [Conventional Commits](https://www.conventionalcommits.org/) like:
> - `feat: add new sensor type`
> - `fix: correct pH validation range`
> - `docs: update README with setup instructions`

---

## 🧰 Development Setup

To set up AFTEC for local development:

```bash
git clone https://github.com/combat47/AFTEC.git
cd AFTEC
make install
make test   # verify everything works
