'''
USE [CARSOFT]
GO

/****** Object:  Table [dbo].[CarPrepayOrder]    Script Date: 12/30/2018 13:48:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[CarPrepayOrder](
	[Oid] [int] IDENTITY(1,1) NOT NULL,
	[car_number] [varchar](50) NOT NULL,
	[service_name] [varchar](50) NOT NULL,
	[prepay] [money] NOT NULL,
	[prepay_type] [int] NULL,
	[pay_channel] [int] NULL,
	[order_id] [varchar](50) NOT NULL,
	[query_order_no] [varchar](50) NULL,
	[park_id] [varchar](50) NOT NULL,
	[trade_no] [varchar](50) NOT NULL,
	[query_time] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[Oid] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO
'''