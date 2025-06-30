-- Inserção de pedidos e itens fictícios
INSERT INTO pedidos (usuario_id, data) VALUES
(1, '2025-06-01'),
(2, '2025-06-02');

INSERT INTO itens_pedido (pedido_id, produto_id, quantidade) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 2, 1),
(2, 4, 3);
