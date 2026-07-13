"""Tests unitarios para las métricas de calidad de embeddings.

Universidad Nacional Mayor de San Marcos
Doctorado en DeepTech — IA y Tecnologías Emergentes
"""

import numpy as np
import pytest
import sys
from pathlib import Path

# Agregar src al path para poder importar metrics
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metrics import (
    compute_trustworthiness,
    compute_continuity,
    compute_stress,
    compute_residual_variance,
    compute_classification_accuracy,
    compute_silhouette,
)

@pytest.fixture
def sample_data():
    """Genera datos sintéticos para testear las funciones."""
    np.random.seed(42)
    n_samples = 50
    X = np.random.randn(n_samples, 5)
    X_embedded = X[:, :2] # Simple proyección lineal como embedding
    y = np.random.randint(0, 2, n_samples)
    return X, X_embedded, y

def test_trustworthiness(sample_data):
    X, X_embedded, _ = sample_data
    val = compute_trustworthiness(X, X_embedded, n_neighbors=5)
    assert isinstance(val, float)
    assert 0.0 <= val <= 1.0

def test_continuity(sample_data):
    X, X_embedded, _ = sample_data
    val = compute_continuity(X, X_embedded, n_neighbors=5)
    assert isinstance(val, float)
    assert 0.0 <= val <= 1.0

def test_stress(sample_data):
    X, X_embedded, _ = sample_data
    val = compute_stress(X, X_embedded)
    assert isinstance(val, float)
    assert val >= 0.0

def test_residual_variance(sample_data):
    X, X_embedded, _ = sample_data
    val = compute_residual_variance(X, X_embedded)
    assert isinstance(val, float)
    assert 0.0 <= val <= 1.0

def test_classification_accuracy(sample_data):
    _, X_embedded, y = sample_data
    val_knn = compute_classification_accuracy(X_embedded, y, classifier='knn', cv=3)
    val_svm = compute_classification_accuracy(X_embedded, y, classifier='svm', cv=3)
    assert isinstance(val_knn, float)
    assert isinstance(val_svm, float)
    assert 0.0 <= val_knn <= 1.0
    assert 0.0 <= val_svm <= 1.0

def test_silhouette(sample_data):
    _, X_embedded, y = sample_data
    val = compute_silhouette(X_embedded, y)
    assert isinstance(val, float)
    assert -1.0 <= val <= 1.0
