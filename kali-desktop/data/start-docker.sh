#!/bin/bash
systemctl daemon-reload
systemctl enable vncserver.service
systemctl enable novnc.service
systemctl start vncserver.service
systemctl start novnc.service