# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgoncal2 <fgoncal2@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 16:07:53 by fgoncal2          #+#    #+#              #
#    Updated: 2026/01/08 16:23:11 by fgoncal2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
	n = int(input("Days until harvest: "))
	def	helper(days):
		if days > n:
			print("Harvest time!")
			return
		else:
			print(f"Day {days}")
			helper(days + 1)
	helper(1)