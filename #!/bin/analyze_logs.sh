#!/bin/bash

# Find incomplete orders (no FILL or CANCEL)
echo "Incomplete Orders:"
grep "ORDER_ID" logs.txt | grep -v "FILL" | grep -v "CANCEL" | awk '{print $1}' | sort | uniq

echo ""
echo "Order Event Counts:"
grep "STATUS" logs.txt | awk '{print $2}' | sort | uniq -c

echo ""
echo "Sample Trace for ORDER_ID=10:"
grep "ORDER_ID=10" logs.txt
