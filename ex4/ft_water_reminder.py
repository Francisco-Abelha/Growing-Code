# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgoncal2 <fgoncal2@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 15:55:52 by fgoncal2          #+#    #+#              #
#    Updated: 2026/01/08 16:24:10 by fgoncal2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	days = int(input("Days since last watering: "))
	if (days > 2):
		print("Water the plants!")
	else:
		print("Plants are fine")