# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgoncal2 <fgoncal2@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 16:35:17 by fgoncal2          #+#    #+#              #
#    Updated: 2026/01/08 16:37:45 by fgoncal2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
	name = input("Enter garden name: ")
	number = input("Enter number of plants: ")
	print(f"Garden: {name}")
	print(f"Plants: {number}")
	print("Status: Growing well!")