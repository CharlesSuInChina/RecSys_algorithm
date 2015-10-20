# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

import method


def test100k_explicit():
    test_count = 5
    evaluation_base = 2
    ans = [0] * evaluation_base
    for k in xrange(1, test_count + 1):
        method.generate_data_100k_explicit(k)
        method.generate_matrix(implicit=False)
        b = method.evaluate_explicit()
        for x in xrange(evaluation_base):
            ans[x] += b[x]
    for x in xrange(evaluation_base):
        ans[x] /= test_count
    print ans


def test100k_implicit():
    test_count = 5
    evaluation_base = 4
    ans = [0] * evaluation_base
    for k in xrange(1, test_count + 1):
        method.generate_data_100k_implicit(k)
        method.generate_matrix(implicit=True)
        b = method.evaluate_implicit()
        for x in xrange(evaluation_base):
            ans[x] += b[x]
    for x in xrange(evaluation_base):
        ans[x] /= test_count
    print ans


def test1m_explicit():
    test_count = 8
    evaluation_base = 2
    ans = [0] * evaluation_base
    for k in xrange(test_count):
        method.generate_data_1m_explicit(test_count, k)
        method.generate_matrix(implicit=False)
        b = method.evaluate_explicit()
        for x in xrange(evaluation_base):
            ans[x] += b[x]
    for x in xrange(evaluation_base):
        ans[x] /= test_count
    print ans


def test1m_implicit():
    test_count = 8
    evaluation_base = 4
    ans = [0] * evaluation_base
    for k in xrange(test_count):
        method.generate_data_1m_implicit(test_count, k)
        method.generate_matrix(implicit=True)
        b = method.evaluate_implicit()
        for x in xrange(evaluation_base):
            ans[x] += b[x]
    for x in xrange(evaluation_base):
        ans[x] /= test_count
    print ans


def test_latest_small_explicit():
    test_count = 8
    evaluation_base = 2
    ans = [0] * evaluation_base
    for k in xrange(test_count):
        method.generate_data_latest_small_explicit(test_count, k)
        method.generate_matrix(implicit=False)
        b = method.evaluate_explicit()
        for x in xrange(evaluation_base):
            ans[x] += b[x]
    for x in xrange(evaluation_base):
        ans[x] /= test_count
    print ans


def test_latest_small_implicit():
    test_count = 8
    evaluation_base = 4
    ans = [0] * evaluation_base
    for k in xrange(test_count):
        method.generate_data_latest_small_implicit(test_count, k)
        method.generate_matrix(implicit=True)
        b = method.evaluate_implicit()
        for x in xrange(evaluation_base):
            ans[x] += b[x]
    for x in xrange(evaluation_base):
        ans[x] /= test_count
    print ans


if __name__ == '__main__':
    test100k_explicit()
    # test100k_implicit()
    # test1m_explicit()
    # test1m_implicit()
    # test_latest_small_explicit()
    # test_latest_small_implicit()
